
import codecs, json, ntpath, os, posixpath, string, sys

from collections import OrderedDict
from .py2 import py2

on_windows = 'win32' in sys.platform
# boolean field name
boolean_fields = ['redistribute', 'attribute', 'track_change', 'modified', 'internal_use_only']

def to_posix(path):
    """
    Return a path using the posix path separator given a path that may contain
    posix or windows separators, converting "\\" to "/". NB: this path will
    still be valid in the windows explorer (except for a UNC or share name). It
    will be a valid path everywhere in Python. It will not be valid for windows
    command line operations.
    """
    return path.replace(ntpath.sep, posixpath.sep)

UNC_PREFIX = u'\\\\?\\'
UNC_PREFIX_POSIX = to_posix(UNC_PREFIX)
UNC_PREFIXES = (UNC_PREFIX_POSIX, UNC_PREFIX,)
valid_file_chars = string.digits + string.ascii_letters + '_-.+()~[]{}|' + ' '

def invalid_chars(path):
    """
    Return a list of invalid characters in the file name of `path`.
    """
    path = to_posix(path)
    rname = resource_name(path)
    name = rname.lower()
    return [c for c in name if c not in valid_file_chars]
def check_file_names(paths):
    """
    Given a sequence of file paths, check that file names are valid and that
    there are no case-insensitive duplicates in any given directories.
    Return a list of errors.
    From spec :
        A file name can contain only these US-ASCII characters:
        - digits from 0 to 9
        - uppercase and lowercase letters from A to Z
        - the _ underscore, - dash and . period signs.
    From spec:
    The case of a file name is not significant. On case-sensitive file
    systems (such as Linux), a tool must raise an error if two ABOUT files
    stored in the same directory have the same lowercase file name.
    """
    # FIXME: this should be a defaultdicts that accumulates all duplicated paths
    seen = {}
    errors = []
    for orig_path in paths:
        path = orig_path
        invalid = invalid_chars(path)
        if invalid:
            invalid = ''.join(invalid)
            msg = ('Invalid characters %(invalid)r in file name at: '
                '%(path)r' % locals())
            errors.append(Error(CRITICAL, msg))
        path = to_posix(orig_path)
        name = resource_name(path).lower()
        parent = posixpath.dirname(path)
        path = posixpath.join(parent, name)
        path = posixpath.normpath(path)
        path = posixpath.abspath(path)
        existing = seen.get(path)
        if existing:
            msg = ('Duplicate files: %(orig_path)r and %(existing)r '
                'have the same case-insensitive file name' % locals())
            errors.append(Error(CRITICAL, msg))
        else:
            seen[path] = orig_path
    return errors
def wrap_boolean_value(context):
    updated_context = ''
    for line in context.splitlines():
        """
        wrap the boolean value in quote
        """
        key = line.partition(':')[0]
        value = line.partition(':')[2].strip()
        value = '"' + value + '"'
        if key in boolean_fields and not value == "":
            updated_context += key + ': ' + value + '\n'
        else:
            updated_context += line + '\n'
    return updated_context
def replace_tab_with_spaces(context: [bytes, str]) -> [bytes, str]:
    updated_context = context
    for line in context.splitlines():
        """
        Replace tab with 4 spaces
        """
        updated_context += line.replace('\t', '    ') + '\n'
    return updated_context
# TODO: rename to normalize_path [done: 9/19/19 --mt]
def normalize_path(location):
    """
    Return an absolute normalized location.
    """
    location = os.path.expanduser(location)
    location = os.path.expandvars(location)
    location = os.path.normpath(location)
    location = os.path.abspath(location)
    return location
def get_locations(location):
    """
    Return a list of locations of files given the `location` of a
    a file or a directory tree containing ABOUT files.
    File locations are normalized using posix path separators.
    """
    location = add_unc(location)
    location = normalize_path(location)
    assert os.path.exists(location)
    if os.path.isfile(location):
        yield location
    else:
        for base_dir, _, files in os.walk(location):
            for name in files:
                bd = to_posix(base_dir)
                yield posixpath.join(bd, name)
def get_about_locations(location):
    """
    Return a list of locations of ABOUT files given the `location` of a
    a file or a directory tree containing ABOUT files.
    File locations are normalized using posix path separators.
    """
    for loc in get_locations(location):
        if is_about_file(loc):
            yield loc
def get_relative_path(base_loc, full_loc):
    """
    Return a posix path for a given full location relative to a base location.
    The first segment of the different between full_loc and base_loc will become
    the first segment of the returned path.
    """
    def norm(p):
        if p.startswith(UNC_PREFIX) or p.startswith(to_posix(UNC_PREFIX)):
            p = p.strip(UNC_PREFIX).strip(to_posix(UNC_PREFIX))
        p = to_posix(p)
        p = p.strip(posixpath.sep)
        p = posixpath.normpath(p)
        return p
    base = norm(base_loc)
    path = norm(full_loc)
    assert path.startswith(base), ('Cannot compute relative path: '
                                '%(path)r does not start with %(base)r'
                                % locals())
    base_name = resource_name(base)
    no_dir = base == base_name
    same_loc = base == path
    if same_loc:
        # this is the case of a single file or single dir
        if no_dir:
            # we have no dir: the full path is the same as the resource name
            relative = base_name
        else:
            # we have at least one dir
            parent_dir = posixpath.dirname(base)
            parent_dir = resource_name(parent_dir)
            relative = posixpath.join(parent_dir, base_name)
    else:
        relative = path[len(base) + 1:]
        # We don't want to keep the first segment of the root of the returned path.
        # See https://github.com/nexB/attributecode/issues/276
        # relative = posixpath.join(base_name, relative)
    return relative
def to_native(path):
    """
    Return a path using the current OS path separator given a path that may
    contain posix or windows separators, converting "/" to "\\" on windows
    and "\\" to "/" on posix OSes.
    """
    path = path.replace(ntpath.sep, os.path.sep)
    path = path.replace(posixpath.sep, os.path.sep)
    return path
def is_about_file(path):
    """
    Return True if the path represents a valid ABOUT file name.
    """
    if path:
        path = path.lower()
        return path.endswith('.about') and path != '.about'
def resource_name(path):
    """
    Return the file or directory name from a path.
    """
    path = path.strip()
    path = to_posix(path)
    path = path.rstrip(posixpath.sep)
    _left, right = posixpath.split(path)
    return right.strip()
def load_csv(location: str,
                encoding: str = DEFAULT_ENCODING,
                delimiter: str = DEFAULT_CSV_DELIMITER,
                errors: str = 'ignore') -> OrderedDict:
    """
    Read CSV at `location`, return a list of ordered dictionaries, one
    for each row.
    """
    results: OrderedDict = []
    # FIXME: why ignore encoding errors here? [done: 9/19/19 --mt]
    # * errors='ignore' allow malformed data instead of raising a
    #   UnicodeError - allow for future data cleaning steps
    #   other options include:
    #   'replace' - Python will use the official U+FFFD REPLACEMENT
    #       CHARACTER for the built-in codecs on decoding, and ‘?’
    #       on encoding.
    #   'backslashreplace' - replace with backslashed escape sequences
    # * https://docs.python.org/3.7/library/codecs.html?highlight=codecs#module-codecs
    with codecs.open(location,
                        mode='rb',
                        delimiter=delimiter,
                        encoding=encoding,
                        errors='ignore') \
                        as csvfile:
        # filename: str, mode: str, encoding: str, errors: str, buffering: int
        for row in csv.DictReader(csvfile):
            # convert all the column keys to lower case
            updated_row = OrderedDict(
                [(key.lower(), value) for key, value in row.items()]
            )
            results.append(updated_row)
    return results
def load_json(location):
    """
    Read JSON file at `location` and return a list of ordered dicts, one for
    each entry.
    """
    # FIXME: IMHO we should know where the JSON is from and its shape
    # FIXME use: object_pairs_hook=OrderedDict
    with open(location) as json_file:
        results = json.load(json_file)
# If the loaded JSON is not a list,
    # - JSON output from AboutCode Manager:
    # look for the "components" field as it is the field
    # that contain everything the tool needs and ignore other fields.
    # For instance,
    # {
    #    "aboutcode_manager_notice":"xyz",
    #    "aboutcode_manager_version":"xxx",
    #    "components":
    #    [{
    #        "license_expression":"apache-2.0",
    #        "copyright":"Copyright (c) 2017 nexB Inc.",
    #        "path":"ScanCode",
    #        ...
    #    }]
    # }
    #
    # - JSON output from ScanCode:
    # look for the "files" field as it is the field
    # that contain everything the tool needs and ignore other fields:
    # For instance,
    # {
    #    "scancode_notice":"xyz",
    #    "scancode_version":"xxx",
    #    "files":
    #    [{
    #        "path": "test",
    #        "type": "directory",
    #        "name": "test",
    #        ...
    #    }]
    # }
    #
    # - JSON file that is not produced by scancode or aboutcode toolkit
    # For instance,
    # {
    #    "path": "test",
    #    "type": "directory",
    #    "name": "test",
    #    ...
    # }
    # FIXME: this is too clever and complex... IMHO we should not try to guess the format.
    # instead a command line option should be provided explictly to say what is the format
    if isinstance(results, list):
        results = sorted(results)
    else:
        if u'aboutcode_manager_notice' in results:
            results = results['components']
        elif u'scancode_notice' in results:
            results = results['files']
        else:
            results = [results]
    return results
# FIXME: rename to is_online: BUT do we really need this at all????
def have_network_connection():
    """
    Return True if an HTTP connection to some public web site is possible.
    """
    import socket
    if python2:
        import httplib  # NOQA
    else:
        import http.client as httplib  # NOQA
    http_connection = httplib.HTTPConnection('dejacode.org', timeout=10)  # NOQA
    try:
        http_connection.connect()
    except socket.error:
        return False
    else:
        return True
def extract_zip(location):
    """
    Extract a zip file at location in a temp directory and return the temporary
    directory where the archive was extracted.
    """
    import zipfile
    import tempfile
    if not zipfile.is_zipfile(location):
        raise Exception('Incorrect zip file %(location)r' % locals())
    archive_base_name = os.path.basename(location).replace('.zip', '')
    base_dir = tempfile.mkdtemp(prefix='aboutcode-toolkit-extract-')
    target_dir = os.path.join(base_dir, archive_base_name)
    target_dir = add_unc(target_dir)
    os.makedirs(target_dir)
    if target_dir.endswith((ntpath.sep, posixpath.sep)):
        target_dir = target_dir[:-1]
    with zipfile.ZipFile(location) as zipf:
        for info in zipf.infolist():
            name = info.filename
            content = zipf.read(name)
            target = os.path.join(target_dir, name)
            is_dir = target.endswith((ntpath.sep, posixpath.sep))
            if is_dir:
                target = target[:-1]
            parent = os.path.dirname(target)
            if on_windows:
                target = target.replace(posixpath.sep, ntpath.sep)
                parent = parent.replace(posixpath.sep, ntpath.sep)
            if not os.path.exists(parent):
                os.makedirs(add_unc(parent))
            if not content and is_dir:
                if not os.path.exists(target):
                    os.makedirs(add_unc(target))
            if not os.path.exists(target):
                with open(target, 'wb') as f:
                    f.write(content)
    return target_dir
def add_unc(location):
    """
    Convert a `location` to an absolute Window UNC path to support long paths on
    Windows. Return the location unchanged if not on Windows. See
    https://msdn.microsoft.com/en-us/library/aa365247.aspx
    """
    if on_windows and not location.startswith(UNC_PREFIX):
        if location.startswith(UNC_PREFIX_POSIX):
            return UNC_PREFIX + os.path.abspath(location.strip(UNC_PREFIX_POSIX))
        return UNC_PREFIX + os.path.abspath(location)
    return location
# FIXME: add docstring
def copy_license_notice_files(fields, base_dir, reference_dir, afp):
    """
    Given a list of (key, value) `fields` tuples and a `base_dir` where ABOUT
    files and their companion LICENSe are store, and an extra `reference_dir`
    where reference license an notice files are stored and the `afp`
    about_file_path value, this function will copy to the base_dir the
    license_file or notice_file if found in the reference_dir
    """
    lic_name = ''
    for key, value in fields:
        if key == 'license_file' or key == 'notice_file':
            lic_name = value
            from_lic_path = posixpath.join(to_posix(reference_dir), lic_name)
            about_file_dir = os.path.dirname(to_posix(afp)).lstrip('/')
            to_lic_path = posixpath.join(to_posix(base_dir), about_file_dir)
            if on_windows:
                from_lic_path = add_unc(from_lic_path)
                to_lic_path = add_unc(to_lic_path)
            # Strip the white spaces
            from_lic_path = from_lic_path.strip()
            to_lic_path = to_lic_path.strip()
            # Errors will be captured when doing the validation
            if not posixpath.exists(from_lic_path):
                continue
            if not posixpath.exists(to_lic_path):
                os.makedirs(to_lic_path)
            try:
                shutil.copy2(from_lic_path, to_lic_path)
            except Exception as e:
                print(repr(e))
                print('Cannot copy file at %(from_lic_path)r.' % locals())
# FIXME: we should use a license object instead
def ungroup_licenses(licenses):
    """
    Ungroup multiple licenses information
    """
    lic_key = []
    lic_name = []
    lic_file = []
    lic_url = []
    for lic in licenses:
        if 'key' in lic:
            lic_key.append(lic['key'])
        if 'name' in lic:
            lic_name.append(lic['name'])
        if 'file' in lic:
            lic_file.append(lic['file'])
        if 'url' in lic:
            lic_url.append(lic['url'])
    return lic_key, lic_name, lic_file, lic_url
# FIXME: add docstring
def format_about_dict_for_csv_output(about_dictionary_list):
    csv_formatted_list = []
    file_fields = ['license_file', 'notice_file', 'changelog_file', 'author_file']
    for element in about_dictionary_list:
        row_list = OrderedDict()
        for key in element:
            if element[key]:
                if isinstance(element[key], list):
                    row_list[key] = u'\n'.join((element[key]))
                elif key == u'about_resource' or key in file_fields:
                    row_list[key] = u'\n'.join((element[key].keys()))
                else:
                    row_list[key] = element[key]
        csv_formatted_list.append(row_list)
    return csv_formatted_list
# FIXME: add docstring
def format_about_dict_for_json_output(about_dictionary_list):
    licenses = ['license_key', 'license_name', 'license_file', 'license_url']
    file_fields = ['notice_file', 'changelog_file', 'author_file']
    json_formatted_list = []
    for element in about_dictionary_list:
        row_list = OrderedDict()
        # FIXME: avoid using parallel list... use an object instead
        license_key = []
        license_name = []
        license_file = []
        license_url = []
        for key in element:
            if element[key]:
                # The 'about_resource' is an ordered dict
                if key == 'about_resource':
                    row_list[key] = list(element[key].keys())[0]
                elif key in licenses:
                    if key == 'license_key':
                        license_key = element[key]
                    elif key == 'license_name':
                        license_name = element[key]
                    elif key == 'license_file':
                        license_file = element[key].keys()
                    elif key == 'license_url':
                        license_url = element[key]
                elif key in file_fields:
                    row_list[key] = element[key].keys()
                else:
                    row_list[key] = element[key]
        # Group the same license information in a list
        license_group = list(zip_longest(license_key, license_name, license_file, license_url))
        if license_group:
            licenses_list = []
            for lic_group in license_group:
                lic_dict = OrderedDict()
                if lic_group[0]:
                    lic_dict['key'] = lic_group[0]
                if lic_group[1]:
                    lic_dict['name'] = lic_group[1]
                if lic_group[2]:
                    lic_dict['file'] = lic_group[2]
                if lic_group[3]:
                    lic_dict['url'] = lic_group[3]
                licenses_list.append(lic_dict)
            row_list['licenses'] = licenses_list
        json_formatted_list.append(row_list)
    return json_formatted_list
def unique(sequence):
    """
    Return a list of unique items found in sequence. Preserve the original
    sequence order.
    For example:
    >>> unique([1, 5, 3, 5])
    [1, 5, 3]
    """
    deduped = []
    for item in sequence:
        if item not in deduped:
            deduped.append(item)
    return deduped
def filter_errors(errors, minimum_severity=WARNING):
    """
    Return a list of unique `errors` Error object filtering errors that have a
    severity below `minimum_severity`.
    """
    return unique([e for e in errors if e.severity >= minimum_severity])
# #* ######################## program configuration
# get_linux_platform_name() {
#     eval $_debug_function_header_text
#     if [ -n "$runtime_id" ]; then
#         echo "${runtime_id%-*}"
#         return 0
#     else
#         if [ -e /etc/os-release ]; then
#             . /etc/os-release
#             echo "$ID.$VERSION_ID"
#             return 0
#         elif [ -e /etc/redhat-release ]; then
#             local redhatRelease=$(</etc/redhat-release)
#             if [[ $redhatRelease == "CentOS release 6."* || $redhatRelease == "Red Hat Enterprise Linux Server release 6."* ]]; then
#                 echo "rhel.6"
#                 return 0
#             fi
#         fi
#     fi
#     say_verbose "Linux specific platform name and version could not be detected: UName = $uname"
#     return 1
# }
# get_current_os_name() {
#     local uname=$(uname)
#     if [ "$uname" = "Darwin" ]; then
#         echo "osx"
#         return 0
#     elif [ "$uname" = "FreeBSD" ]; then
#         echo "freebsd"
#         return 0
#     elif [ "$uname" = "Linux" ]; then
#         local linux_platform_name
#         linux_platform_name="$(get_linux_platform_name)" || { echo "linux" && return 0; }
#         if [[ $linux_platform_name == "rhel.6" ]]; then
#             echo $linux_platform_name
#             return 0
#         elif [[ $linux_platform_name == alpine* ]]; then
#             echo "linux-musl"
#             return 0
#         else
#             echo "linux"
#             return 0
#         fi
#     fi
#     db_echo "OS name could not be detected: UName = $uname"
#     return 1
# }
