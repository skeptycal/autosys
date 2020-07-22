#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Part of the `AutoSys` package
        copyright (c) 2019 Michael Treanor
        https://www.github.com/skeptycal/autosys
        https://www.twitter.com/skeptycal

    `AutoSys` is licensed under the `MIT License
        `<https://opensource.org/licenses/MIT>`
    """
if True:  # !------------------------ Imports
    import sys
    import platform
    import subprocess

    from platform import system as OS
    from subprocess import CalledProcessError
    from typing import List, Tuple

    from autosys import NL, ARGS, __version__ as VERSION, __title__ as APP_NAME

    from autosys.debug import br, hr, dbprint

    _debug_: bool = True  # True => use Debug features
    __all__: List[str] = []

if OS().startswith("Darwin"):  # !------------------------ Classes

    class MacOS:
        """
        Provides an interface to interact with macOS.
        """

        OSA_TEST = """
            tell application "System Events"
                set processName to name of processes whose frontmost is true
                do shell script "echo " & processName
            end tell
            """

        OSA_GET_CHROME_ACTIVE_URL = """
            tell application "Google Chrome" to return URL of active tab of front window
            """

        def __init__(self):
            self._set_os_info()

        def _set_os_info(self):
            self.py_vers = platform.python_version_tuple()
            self.platform = platform.platform().split("-")
            self.py3 = int(self.py_vers[0]) > 2

        def clipboard_copy(self, data: str):
            subprocess.run(
                "pbcopy",
                universal_newlines=True,
                capture_output=True,
                input=data,
            )

        def osascript(self, applescript: str = OSA_GET_CHROME_ACTIVE_URL):
            """ Return result of applesript. """
            args = [
                item
                for x in [
                    ("-e", l.strip())
                    for l in applescript.split("\n")
                    if l.strip() != ""
                ]
                for item in x
            ]
            proc = subprocess.Popen(
                ["osascript"] + args, stdout=subprocess.PIPE
            )
            progname = proc.stdout.read().strip()
            # sys.stdout.write(str(progname))

        def get_chrome_url(self, clipboard=False):
            """ Return URL from active tab of Google Chrome to macOS clipboard.

                TODO - copy URL to clipboard
                """
            # set <url> to active Chrome tab url
            print(f"{MacOS.OSA_GET_CHROME_ACTIVE_URL=}")
            url = self.osascript(MacOS.OSA_GET_CHROME_ACTIVE_URL)
            print(f"{url=}")

            # copy to clipboard
            if clipboard:
                self.clipboard_copy(self, url)

            # -v is verbose : if -v ... print url to stdout in addition
            # ["$1" = '-q'] | | printf "%s\n" "$url"

        def get_shell_output(self, s: str):
            try:
                return subprocess.check_call(s, shell=True)
            except CalledProcessError as e:
                return e

        def get_shell_output(self, data: List[str] = (["ls", "-1"])):
            return subprocess.check_output(data)

    m = MacOS()
    # from autosys._version import *
    # objects exported for 'import *'
    __all__.extend(["MacOS", "m"])

if True:  # !------------------------ Script Tests

    def _tests_():
        """ Debug Tests for script. """
        pass
        print(f"{OS()=}")
        br()
        print(f"{__all__=}")
        print(f"{m.platform=}")
        print(f"{m.get_chrome_url()=}")


def _main_():  # !------------------------ Script Main
    """
    CLI script main entry point.
    """
    if _debug_:
        _tests_()


if __name__ == "__main__":
    # ARGS.append('version')  # ! test
    ARGS.append("help")  # ! test
    if "version" in ARGS:
        print(f"{APP_NAME} version {VERSION}")
    else:
        if "help" in ARGS or "debug" in ARGS:
            _debug_ = True
        _main_()
"""

    . $(which ssm)
    declare -g PREVIOUS_URL
    PREVIOUS_URL=''


    getURL() {
        # copy URL from active tab of Google Chrome to macOS clipboard
        if [[ $OS = 'darwin' ]]; then
            # set <url> to active Chrome tab url
            url=$(osascript -e 'tell application "Google Chrome" to return URL of active tab of front window')

            # copy to clipboard
            printf "%s" "$url" | pbcopy

            # -v is verbose : if -v ... print url to stdout in addition
            [ "$1" = '-q' ] || printf "%s\n" "$url"
        fi
        }

    ping_avg() {
        usage="$0 [-h] | [COUNT URL]"
        case $1 in
            '-h'|'--help'|'help')
                me $usage
                exit
                ;;
            *)
                # extract the average ping time (ms) from 'ping' output
                # $1 = number of pings to average
                count=$1

                # $2 = url to test
                # remove schema and folders
                url_short=$(echo "$2" | cut -d '/' -f 3)

                # ww
                ping -c "$count" "$url_short" | tail -n 1 | cut -d '/' -f 6
                ;;
        esac
        }

    log_urls() {
        declare -g usage="log_urls [COUNT] [SLEEP_TIME] [URL_LOG]"

        if [ "$1" = '-h' ]; then
            ce "$usage"
        else
            # number of repeats for average ping measurement - default 2
            declare -g count=${1:-2}

            # time to sleep between checks                   - default 10s
            declare -g sleep_time=${2:-10}

            # location of log file                           - default ~/.url_log.log
            declare -g url_log=${3:-~/.url_log.log}

            # shellcheck disable=SC2078 # ignore constant expression  `while [ : ]`
            while [ : ]
            do
                # get url of Chrome active tab
                declare -g url=$(osascript -e 'tell application "Google Chrome" to return URL of active tab of front window')

                # TODO - check if url = PREVIOUS_URL ... to keep down the spam
                if [[ $url = "$PREVIOUS_URL" ]]; then
                    true #TODO do stuff if $url is the same ...
                else
                    PREVIOUS_URL=$url
                fi

                # remove schema and folders
                declare -g url_short=$(echo "$url" | cut -d '/' -f 3)

                # comparison site
                # comp="www.example.com"
                # comp="www.google.com"
                # comp="192.168.1.100"
                declare -g comp="skeptycal.com"

                # test ping of site
                # ping -c "$count" "$url_short" | tail -n 1 | cut -d '/' -f 6

                me "$(date), $url, $(ping_avg $count $url), $(ping_avg $count $comp)" >&2

                # log to $url_log
                printf "%s\n" "$(date), $url, $(ping_avg $count $url), $(ping_avg $count $comp)" >>$url_log

                sleep $sleep_time
            done
        fi
        unset url_short count comp sleep_time
    }


    """
