#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
""" repo.py - setup, commit, build, test, upload ... with Python!
    - Assuming Git, Python, Poetry are installed

        import repo or use with the following CLI syntax:

    Usage:
        repo [NAME] [-z]
        repo [NAME] [-q | -v ] [--pattern PATTERN]
        repo [--help | --version | --debug]

    Options:
        NAME                           Repo name (default is folder name)
        -l <type>, --license <type>    Choose license type    [default: MIT]
        -d <path>, --directory <path)  Choose path for repo   [default: current]
        -u, --upload                   Upload to pypi         [default: False]

        -q, --quiet             Suppress most error messages  [default: True]
        -v, --verbose           Display detailed progress     [default: False]


        --version               Show version.
        --debug                 Show debug info and test results.
        -h, --help              Show this screen.

    Exit status:

        0 if all file names were printed without issue.
        1 otherwise.

    Based on ANSI standard ECMA-48:
    http://www.ecma-international.org/publications/files/ECMA-ST/Ecma-048.pdf
    Unicode characters based on the Official Unicode Consortium code chart
    https://www.unicode.org/charts/PDF/U2580.pdf

    NOTE: if getting this error:
    'ImportError: attempted relative import with no known parent package'

    Solution #1: Run your script using python3 -m
    Solution #2: Set __package__ manually (this sucks, really)
    Solution #3: Use absolute imports and setuptools
    """


if True:  # !-------------------> Imports
    import time
    import textwrap
    from textwrap import dedent
    from sys import argv
    from pathlib import Path
    from typing import Any, Dict, List, Set, Tuple
    from docopt import docopt

if True:  # !-------------------> Constants
    PACKAGE_NAME: str = "AutoSys"
    PACKAGE_PREFIX: str = f"{PACKAGE_NAME} -> "
    UNDEFINED = object()


def headerprint(*args, **kwargs):  # print a text border before *args
    print("_" * 79)
    print(*args, **kwargs)


def trace_it(func):  # trace decorator
    pass


def timeit(method):  # timer decorator
    def timed(*args, **kwargs):
        t0 = time.time()
        retval = method(*args, **kwargs)
        dt = (time.time() - t0) * 1000
        print(
            f"{PACKAGE_PREFIX} {__name__} - Method {method.__name__} took {dt:3.3f} ms."
        )
        print(f"{PACKAGE_PREFIX}Method {method.__name__} returned {retval}.")
        return result

    return timed


def entry_exit(f):  # PythonDecorators/entry_exit_function.py
    def new_f():
        print("Entering", f.__name__)
        retval = f()
        print("Exited", f.__name__)

    return new_f


class NamedDict(dict):
    """ ### class NamedDict

        Standard python dictionary with a <name> property added so that the object knows it's own name. This is a drop-in replacement for `dict`.
        ```
        NamedDict()
            - new empty dictionary dict(mapping)
            - new dictionary initialized from a mapping object's (key, value) pairs dict(iterable)
            - new dictionary initialized as if via: d = {} for k, v in iterable: d[k] = v dict(**kwargs)
            - new dictionary initialized with the name=value pairs in the keyword argument list. For example: dict(one=1, two=2)
        ```
        """

    def __init__(self, *args, **kwargs):
        try:
            self._name = kwargs.pop("name")
        except KeyError:
            raise KeyError('a "name" keyword argument must be supplied')
        super(NamedDict, self).__init__(*args, **kwargs)

    @classmethod
    def fromkeys(cls, name, seq, value=None):
        """ Create a new <NamedDict> dictionary with keys from iterable and values set to value. """
        return cls(dict.fromkeys(seq, value), name=name)

    @property
    def name(self):
        """ Returns the name of the NamedDict dictionary. """
        return self._name


class TextFile(str):
    """ #### TextFile class

        A subclass of the string type with features to track files. It is specifically designed to handle configuration files used in development and CI pipelines, but any text file can be tracked and modified.

        str(object='') -> str str(bytes_or_buffer[, encoding[, errors]]) -> str

        Create a new TextFile object from the given object. If encoding or errors is specified, then the object must expose a data buffer that will be decoded using the given encoding and error handler. Otherwise, returns the result of object.__str__() (if defined) or repr(object). encoding defaults to sys.getdefaultencoding(). errors defaults to 'strict'.

        """

    def __init__(self):
        super().__init__()

    def _get_lines(self, keepends=False):
        for _ in self.splitlines(self, keepends=keepends):
            yield _

    def head(self, lines=5):
        return self._get_lines()[0:lines]

    def tail(self, lines=5):
        return self._get_lines()[::-1][0:lines]

    def show(self, lines=5, numbers=False, width=79):
        for _ in range(lines):
            return self._get_lines(5)


class Repo:
    """ Python module and repository manager.
        """

    def __init__(self, repo_name: str = ""):
        """ Set initial repo name, usage text, setup path, etc.

            Returns a list of values set without errors. By default,
            overwriting values is prohibited. Set <force> to True
            to overwrite class values.
            """
        super().__init__()
        self.Path: Path = Path(__file__).resolve()
        self.script_path: str = self.Path.as_posix()
        self.repo_name: str
        if repo_name == "":
            self.repo_name = Path().name
        else:
            self.repo_name = repo_name
        self.module_name: str = f"{repo_name}.py"
        self.module_path = f"{self.script_path}/{self.repo_name}"
        self.module_file: str = f"{self.module_path}/{self.module_name}"
        self.repo_usage = __doc__  # TODO should be from python file

    def _create_files(self):
        Path.touch()

    # !------------------------------> utility methods

    def _setup_directory_structure(self, project_name: str):
        """ Create basic directory structure:
            ```
                .
                ├── bak
                ├── docs
                ├── images
                └── tests

            """
        # p = Path(self.script_path).resolve()
        pass

    def _setup_repo_info_files(self):
        pass

    def _setup_repo_dev_files(self):
        pass

    def _print_file_info(self, *args) -> int:
        """ #### Print DEBUG and testing information.

            Use `*args` to pass names of variables or sections to print. Example:

            ```
                if 'basic' in args:
                    headerprint(f"{self.script_path=}")
                    headerprint(f"{self.repo_name=}")
                if 'usage' in args:
                    headerprint(self.repo_usage)
                if 'setup' in args:
                    headerprint(self.setup_py())
            """
        retval: int = 0
        # args = []
        # for arg in args_tuple:  # convert to list for DEBUG purposes
        #     args.append(arg)

        # print(type(args))
        # check *args for various arbitrary names that match debug sections
        headerprint("*** DEBUG: printing debug info ...",)
        print("=" * 79)
        for arg in args:  # cycle through <args>
            # various versions of local and global variables
            if arg in ["globals", "locals", "doc", "builtins", "most"]:
                if arg == "doc":
                    fmt = globals().copy().pop("__doc__")
                    print(f"  {arg:25.25}    {fmt}")
                    continue
                if arg == "globals":
                    fmt = globals().copy()
                elif arg == "locals":
                    fmt = locals().copy()
                elif arg == "builtins":
                    fmt = globals().copy().pop("__builtins")
                elif arg == "most":
                    fmt = globals().copy()
                    for k, v in fmt.items():
                        if k == "__builtins__":
                            # try:
                            fmt.pop(k)
                            # except:
                            #     pass
                            continue
                        elif k.startswith("__doc"):
                            fmt.pop(k)
                            continue

                try:
                    for k in fmt.keys():  # print formatted globals()
                        if False:  # k[0] == '_' and k[1] != '_':
                            pass
                        else:
                            print(f"  {k:25.25}    {fmt.get(k)}")
                            print()
                            print("_" * 50)
                    continue
                except:
                    pass  # ! ignoring errors ... this is a dev tool, after all
            elif arg == "basic":  # basic repo information
                headerprint("*** Basic Repo Info:")
                print(f"{self.script_path=}")
                print(f"{self.repo_name=}")
                print(f"{self.module_path=}")
                continue
            elif arg == "usage":  # usage / help screen text
                headerprint(self.repo_usage)
                continue
            elif arg == "setup":  # setup.py script
                headerprint(self.setup_py())
                continue
            else:
                pass  # add more directives here ...
            try:  # print attributes from <args> in <self> if they exist
                headerprint(f"*args({arg})")
                s = self.__getattribute__(arg)
                print(f"  {s}")
            except:
                print(f"  error printing <self.{arg}>")
                retval = 1
                pass  # ! ignoring errors here ! - we just print what we can
        return retval

    # !------------------------------> methods that return file content

    def _readme(self):
        pass

    def _setup_py_min(self) -> str:
        return dedent(
            f"""\
            setup(
                name='{self.repo_name}',
                packages=find_packages(),
            )"""
        )

    def git_ignore(self) -> str:  # --- .gitignore
        return dedent(
            f"""\
            # Project-specific files

            # general ignore files
            *private*
            *bak*

            # Python repo files
            .coveragerc
            .coveralls.yml
            .pre-commit-config.yaml
            .pylintrc
            .travis.yml
            pyproject.toml
            pytest.ini
            tox.ini
            toxcov.ini

            # Python dev files
            .gitconfig
            .gitmodules
            .git*
            .mypy_cache/
            .pytest_cache/
            .vscode/

            # Python build files
            *.py[cod]
            *.egg-ignore
            *.egg-info
            __pycache__/
            build/
            dist/
            env/

            # security
            .pypirc
            *history*
            *hist*
            config.py
            config.json
            sftp.json
            */*.key
        """
        )

    def setup_py(self) -> str:
        return dedent(
            f"""\
        #!/usr/bin/env python3
        # -*- coding: utf-8 -*-
        from __future__ import absolute_import

        from setuptools import setup

        import {self.repo_name}

        setup(
            name={self.repo_name},
            version={self.repo_name}.__version__,
            description="System utilities for Python on macOS",
            long_description=open("README.md").read(),
            author="Michael Treanor",
            author_email="skeptycal@gmail.com",
            maintainer="Michael Treanor",
            maintainer_email="skeptycal@gmail.com",
            url="http://github.com/skeptycal/autosys/",
            license="MIT",
            packages=["autosys"],
            install_requires=[],
            test_require=["tox", "pytest", "coverage", "pytest-cov"],
            test_suite="test",
            zip_safe=False,
            keywords="cli utilities python ai ml text console log debug test testing",
            classifiers=[
                "Development Status :: 5 - Production/Stable",
                "Environment :: Console",
                "Environment :: MacOS X",
                "Environment :: Web Environment",
                "Framework :: Django",
                "Framework :: Flask",
                "Intended Audience :: Developers",
                "License :: OSI Approved :: MIT License",
                "Natural Language :: English",
                "Operating System :: MacOS",
                "Programming Language :: Cython",
                "Programming Language :: Python :: 3.5",
                "Programming Language :: Python :: 3.6",
                "Programming Language :: Python :: 3.7",
                "Programming Language :: Python :: Implementation :: CPython",
                "Programming Language :: Python",
                "Topic :: Software Development :: Libraries :: Python Modules",
                "Topic :: Software Development :: Testing",
                "Topic :: Utilities",
            ],
        )


        """
        )

    def setup_cfg(self):
        pass

    def CODE_OF_CONDUCT_md(self) -> str:
        return dedent(
            """\
        # Contributor Covenant Code of Conduct

        # Our Pledge

        In the interest of fostering an open and welcoming environment, we as
        contributors and maintainers pledge to making participation in our project and
        our community a harassment-free experience for everyone, regardless of age, body
        size, disability, ethnicity, sex characteristics, gender identity and expression,
        level of experience, education, socio-economic status, nationality, personal
        appearance, race, religion, or sexual identity and orientation.

        # Our Standards

        Examples of behavior that contributes to creating a positive environment
        include:

        * Using welcoming and inclusive language
        * Being respectful of differing viewpoints and experiences
        * Gracefully accepting constructive criticism
        * Focusing on what is best for the community
        * Showing empathy towards other community members

        Examples of unacceptable behavior by participants include:

        * The use of sexualized language or imagery and unwelcome sexual attention or
        advances
        * Trolling, insulting/derogatory comments, and personal or political attacks
        * Public or private harassment
        * Publishing others' private information, such as a physical or electronic
        address, without explicit permission
        * Other conduct which could reasonably be considered inappropriate in a
        professional setting

        # Our Responsibilities

        Project maintainers are responsible for clarifying the standards of acceptable
        behavior and are expected to take appropriate and fair corrective action in
        response to any instances of unacceptable behavior.

        Project maintainers have the right and responsibility to remove, edit, or
        reject comments, commits, code, wiki edits, issues, and other contributions
        that are not aligned to this Code of Conduct, or to ban temporarily or
        permanently any contributor for other behaviors that they deem inappropriate,
        threatening, offensive, or harmful.

        # Scope

        This Code of Conduct applies within all project spaces, and it also applies when
        an individual is representing the project or its community in public spaces.
        Examples of representing a project or community include using an official
        project e-mail address, posting via an official social media account, or acting
        as an appointed representative at an online or offline event. Representation of
        a project may be further defined and clarified by project maintainers.

        # Enforcement

        Instances of abusive, harassing, or otherwise unacceptable behavior may be
        reported by contacting the project team at skeptycal@gmail.com. All
        complaints will be reviewed and investigated and will result in a response that
        is deemed necessary and appropriate to the circumstances. The project team is
        obligated to maintain confidentiality with regard to the reporter of an incident.
        Further details of specific enforcement policies may be posted separately.

        Project maintainers who do not follow or enforce the Code of Conduct in good
        faith may face temporary or permanent repercussions as determined by other
        members of the project's leadership.

        # Attribution

        This Code of Conduct is adapted from the [Contributor Covenant][homepage], version 1.4,
        available at https://www.contributor-covenant.org/version/1/4/code-of-conduct.html

        [homepage]: https://www.contributor-covenant.org

        For answers to common questions about this code of conduct, see
        https://www.contributor-covenant.org/faq
        """
        )


# !------------------------------> main entry point


def main():
    """
    CLI script main entry point.
    """
    # print(__version__)
    d = docopt(__doc__, argv)
    repo = Repo("as_repo")
    repo._print_file_info("basic", "repo_name")


if __name__ == "__main__":  # if script is loaded directly from CLI
    main()


# !------------------------------> References
""" Standard repo files
    AUTHORS
    CHANGES.yml
    CODE_OF_CONDUCT.md
    LICENSE
    MANIFEST.in
    README.md
    bak
    docs
    pynow
    pyproject.toml
    pytest.ini
    repo_files
    setup.py
    src
    test
    tox.ini
    toxcov.ini
    """

""" - main folder and code folder both named the same
    - no __init__.py in root


    # example ... pyment: root
    pyment/
    ├── CHANGELOG
    ├── LICENSE
    ├── MANIFEST.in
    ├── Pyment.egg-info/
    ├── README.rst
    ├── build/
    ├── dist/
    ├── doc/
    ├── example.py
    ├── example.py.patch
    ├── example_numpy.py.patch
    ├── pyment/
    ├── pyment.conf
    ├── setup.cfg
    ├── setup.py*
    └── tests/

    6 directories, 10 files

    root files:
    CHANGELOG
    LICENSE
    MANIFEST.in
    README.rst
    setup.cfg
    setup.py*


    # info files
    AUTHORS
        CHANGES.yml -or- CHANGELOG
        LICENSE
        tree.md
        CODE_OF_CONDUCT.md

    # dev config files
        .gitignore
        pyproject.toml
        pytest.ini
        requirements.txt
        test_ < module > .py
        test/
        tox.ini
        toxcov.ini

    # default dev moduless
        autosys
        flake8
        poetry
        pylint
        pytest
        requests
        docopt

    # images
        images/
        Pil

    # python build files
        __init__.py
        <module > .py
        MANIFEST.in
        README.md
        setup.py
        setup.cfg
        src/

    # repo setup files
        bak
        setup.sh
        src/

# utilities (run from PATH)
    modpy
    pynow

# documentation
    (github pages docs / setup)
    _config.yml

    jekyll:

    ├── docs
    │   ├── 404.html
    │   ├── Gemfile
    │   ├── Gemfile.lock
    │   ├── _config.yml
    │   ├── _posts
    │   ├── _site
    │   ├── about.markdown
    │   └── index.markdown
    """

""" details about minimal setup.py
    from setuptools import setup, find_packages
    .
    ├── project
    │   ├── package
    │   │   ├── __init__.py
    │   │   ├── module.py
    │   │   └── standalone.py
    │   └── setup.py

    minimal setup.py:

    setup(
        name='your_package_name',
        packages=find_packages(),
    )
    """
