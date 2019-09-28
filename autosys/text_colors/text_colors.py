#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
""" text_colors version 0.9.3

    The obligatory ANSI text colors implementation.
    Requires Python 3.6+
    """

import syspy
import locale
import os
import sys
import json
from typing import List, Dict, Any


# Initialize constants, variables, strings, etc...
ANSI_CHART = """ANSI Effects Chart
    <code>
    ╔══════════╦════════════════════════════════╦═════════════════════════════════════════════════════════════════════════╗
    ║  Code    ║             Effect             ║                                   Note                                  ║
    ╠══════════╬════════════════════════════════╬═════════════════════════════════════════════════════════════════════════╣
    ║ 0        ║  Reset / Normal                ║  all attributes off                                                     ║
    ║ 1        ║  Bold or increased intensity   ║                                                                         ║
    ║ 2        ║  Faint (decreased intensity)   ║  NWS                                                  ║
    ║ 3        ║  Italic                        ║  NWS Sometimes treated as inverse.                    ║
    ║ 4        ║  Underline                     ║                                                                         ║
    ║ 5        ║  Slow Blink                    ║  less than 150 per minute                                               ║
    ║ 6        ║  Rapid Blink                   ║  MS-DOS ANSI.SYS; 150+ per minute; not widely supported                 ║
    ║ 7        ║  [[reverse video]]             ║  swap foreground and background colors                                  ║
    ║ 8        ║  Conceal                       ║  NWS                                                  ║
    ║ 9        ║  Crossed-out                   ║  Characters legible, but marked for deletion.  NWS    ║
    ║ 10       ║  Primary(default) font         ║                                                                         ║
    ║ 11–19    ║  Alternate font                ║  Select alternate font `n-10`                                           ║
    ║ 20       ║  Fraktur                       ║  hardly ever supported                                                  ║
    ║ 21       ║  Bold off or Double Underline  ║  Bold off not widely supported; double underline hardly ever supported. ║
    ║ 22       ║  Normal color or intensity     ║  Neither bold nor faint                                                 ║
    ║ 23       ║  Not italic, not Fraktur       ║                                                                         ║
    ║ 24       ║  Underline off                 ║  Not singly or doubly underlined                                        ║
    ║ 25       ║  Blink off                     ║                                                                         ║
    ║ 27       ║  Inverse off                   ║                                                                         ║
    ║ 28       ║  Reveal                        ║  conceal off                                                            ║
    ║ 29       ║  Not crossed out               ║                                                                         ║
    ║ 30–37    ║  Set foreground color          ║  See color table below                                                  ║
    ║ 38       ║  Set foreground color          ║  Next arguments are `5;n` or `2;r;g;b`, see below                       ║
    ║ 39       ║  Default foreground color      ║  implementation defined (according to standard)                         ║
    ║ 40–47    ║  Set background color          ║  See color table below                                                  ║
    ║ 48       ║  Set background color          ║  Next arguments are `5;n` or `2;r;g;b`, see below                       ║
    ║ 49       ║  Default background color      ║  implementation defined (according to standard)                         ║
    ║ 51       ║  Framed                        ║                                                                         ║
    ║ 52       ║  Encircled                     ║                                                                         ║
    ║ 53       ║  Overlined                     ║                                                                         ║
    ║ 54       ║  Not framed or encircled       ║                                                                         ║
    ║ 55       ║  Not overlined                 ║                                                                         ║
    ║ 60       ║  ideogram underline            ║  hardly ever supported                                                  ║
    ║ 61       ║  ideogram double underline     ║  hardly ever supported                                                  ║
    ║ 62       ║  ideogram overline             ║  hardly ever supported                                                  ║
    ║ 63       ║  ideogram double overline      ║  hardly ever supported                                                  ║
    ║ 64       ║  ideogram stress marking       ║  hardly ever supported                                                  ║
    ║ 65       ║  ideogram attributes off       ║  reset the effects of all of 60-64                                      ║
    ║ 90–97    ║  Set bright foreground color   ║  aixterm (not in standard)                                              ║
    ║ 100–107  ║  Set bright background color   ║  aixterm (not in standard)                                              ║
    ╚══════════╩════════════════════════════════╩═════════════════════════════════════════════════════════════════════════╝
    </code>
    """

#  38 - Set foreground color - Next arguments are `5;n` or `2;r;g;b`, see below
ANSI_DICT_LIST = [
    {'code': 'Code', 'effect': 'Effect', 'notes': 'Note'},
    {'code': '0', 'effect': 'Reset/Normal', 'notes': 'allattributesoff'},
    {'code': '1', 'effect': 'Boldorincreasedintensity', 'notes': ''},
    {'code': '2', 'effect': 'Faint(decreasedintensity)', 'notes': 'NWS'},
    {'code': '3', 'effect': 'Italic', 'notes': 'NWSSometimestreatedasinverse.'},
    {'code': '4', 'effect': 'Underline', 'notes': ''},
    {'code': '5', 'effect': 'SlowBlink', 'notes': 'lessthan150perminute'},
    {'code': '6', 'effect': 'RapidBlink',
        'notes': 'MS-DOSANSI.SYS;150+perminute;notwidelysupported'},
    {'code': '7', 'effect': '[[reversevideo]]',
        'notes': 'swapforegroundandbackgroundcolors'},
    {'code': '8', 'effect': 'Conceal', 'notes': 'NWS'},
    {'code': '9', 'effect': 'Crossed-out',
        'notes': 'Characterslegible,butmarkedfordeletion.NWS'},
    {'code': '10', 'effect': 'Primary(default)font', 'notes': ''},
    {'code': '11–19', 'effect': 'Alternatefont',
        'notes': 'Selectalternatefont`n-10`'},
    {'code': '20', 'effect': 'Fraktur', 'notes': 'hardlyeversupported'},
    {'code': '21', 'effect': 'BoldofforDoubleUnderline',
        'notes': 'Boldoffnotwidelysupported;doubleunderlinehardlyeversupported.'},
    {'code': '22', 'effect': 'Normalcolororintensity',
        'notes': 'Neitherboldnorfaint'},
    {'code': '23', 'effect': 'Notitalic,notFraktur', 'notes': ''},
    {'code': '24', 'effect': 'Underlineoff',
        'notes': 'Notsinglyordoublyunderlined'},
    {'code': '25', 'effect': 'Blinkoff', 'notes': ''},
    {'code': '27', 'effect': 'Inverseoff', 'notes': ''},
    {'code': '28', 'effect': 'Reveal', 'notes': 'concealoff'},
    {'code': '29', 'effect': 'Notcrossedout', 'notes': ''},
    {'code': '30', 'effect': 'Setforegroundcolor', 'notes': 'BLACK, add ;1m GRAY'},
    {'code': '31', 'effect': 'Setforegroundcolor',
        'notes': 'RED, add ;1m BRIGHTRED'},
    {'code': '32', 'effect': 'Setforegroundcolor',
        'notes': 'GREEN, add ;1m BRIGHTGREEN'},
    {'code': '33', 'effect': 'Setforegroundcolor',
        'notes': 'YELLOW, add ;1m BRIGHTYELLOW'},
    {'code': '34', 'effect': 'Setforegroundcolor',
        'notes': 'BLUE, add ;1m BRIGHTBLUE'},
    {'code': '35', 'effect': 'Setforegroundcolor',
        'notes': 'MAGENTA, add ;1m BRIGHTMAGENTA'},
    {'code': '36', 'effect': 'Setforegroundcolor',
        'notes': 'CYAN, add ;1m BRIGHTCYAN'},
    {'code': '37', 'effect': 'Setforegroundcolor',
        'notes': 'LIGHTGRAY, add ;1m WHITE'},
    # "BLACK": "\u001b[30m",
    # "RED": "\u001b[31m",
    # "GREEN": "\u001b[32m",
    # "BROWN": "\u001b[33m",
    # "BLUE": "\u001b[34m",
    # "MAGENTA": "\u001b[35m",
    # "CYAN": "\u001b[36m",
    # "GRAY": "\u001b[37m",
    # "BBLACK": "\u001b[30;1m",
    # "BRED": "\u001b[31;1m",
    # "BGREEN": "\u001b[32;1m",
    # "BYELLOW": "\u001b[33;1m",
    # "BBLUE": "\u001b[34;1m",
    # "BMAGENTA": "\u001b[35;1m",
    # "BCYAN": "\u001b[36;1m",
    # "BWHITE": "\u001b[37;1m",
    {'code': '38', 'effect': 'Setforegroundcolor',
        'notes': 'Nextargumentsare`5;n`or`2;r;g;b`,seebelow'},
    {'code': '39', 'effect': 'Defaultforegroundcolor',
        'notes': 'implementationdefined(accordingtostandard)'},
    {'code': '40–47', 'effect': 'Setbackgroundcolor', 'notes': 'Seecolortablebelow'},
    {'code': '48', 'effect': 'Setbackgroundcolor',
        'notes': 'Nextargumentsare`5;n`or`2;r;g;b`,seebelow'},
    {'code': '49', 'effect': 'Defaultbackgroundcolor',
        'notes': 'implementationdefined(accordingtostandard)'},
    {'code': '51', 'effect': 'Framed', 'notes': ''},
    {'code': '52', 'effect': 'Encircled', 'notes': ''},
    {'code': '53', 'effect': 'Overlined', 'notes': ''},
    {'code': '54', 'effect': 'Notframedorencircled', 'notes': ''},
    {'code': '55', 'effect': 'Notoverlined', 'notes': ''},
    {'code': '60', 'effect': 'ideogramunderline', 'notes': 'hardlyeversupported'},
    {'code': '61', 'effect': 'ideogramdoubleunderline',
        'notes': 'hardlyeversupported'},
    {'code': '62', 'effect': 'ideogramoverline', 'notes': 'hardlyeversupported'},
    {'code': '63', 'effect': 'ideogramdoubleoverline',
        'notes': 'hardlyeversupported'},
    {'code': '64', 'effect': 'ideogramstressmarking', 'notes': 'hardlyeversupported'},
    {'code': '65', 'effect': 'ideogramattributesoff',
        'notes': 'resettheeffectsofallof60-64'},
    {'code': '90–97', 'effect': 'Setbrightforegroundcolor',
        'notes': 'aixterm(notinstandard)'},
    {'code': '100–107', 'effect': 'Setbrightbackgroundcolor', 'notes': 'aixterm(notinstandard)'}]


# def print_ansi_list():
#     for line in ANSI_DICT_LIST:

        # locale.setlocale(locale.LC_ALL, "")
DEFAULT_ENCODING = locale.getpreferredencoding()

FG_DICT: dict[str, str] = {
    # The first 11 codes are just favorites I picked.
    # Some have short and long names for duplicates.
    # Add more personalized colors by name if desired ...
    "MAIN": "\u001b[38;5;229m",
    "COOL": "\u001b[38;5;38m",
    "MIKES_BLUE": "\u001b[38;5;38m",
    "GO": "\u001b[38;5;28m",
    "GREEN_MEANS_GO": "\u001b[38;5;28m",
    "WARN": "\u001b[38;5;203m",
    "CHERRY": "\u001b[38;5;124m",
    "CANARY": "\u001b[38;5;226m",
    "DANGERWILLROBINSON": "\u001b[38;5;203m",
    "ATTN": "\u001b[38;5;178m",
    "WHATABURGER": "\u001b[38;5;178m",
    "PURPLE": "\u001b[38;5;93m",
    "PURPLEHAZE": "\u001b[38;5;93m",
    "RESET": "\u001b[0m",  # Reset all attributes
    "NEXT_FG": "\u001b[38m",  # Next Foreground in Cycle (rainbow ...)
    "DEF_FG": "\u001b[39m",  # Reset to Default Foreground
    # These are the codes for the foreground 8 color set
    "BLACK": "\u001b[30m",      # 0
    "RED": "\u001b[31m",        # 1
    "GREEN": "\u001b[32m",      # 2
    "BROWN": "\u001b[33m",      # 3
    "BLUE": "\u001b[34m",       # 4
    "MAGENTA": "\u001b[35m",    # 5
    "CYAN": "\u001b[36m",       # 6
    "GRAY": "\u001b[37m",       # 7
    # These are added to the 8-color FG to make the 16 color FG set
    "BBLACK": "\u001b[30;1m",
    "BRED": "\u001b[31;1m",
    "BGREEN": "\u001b[32;1m",
    "BYELLOW": "\u001b[33;1m",
    "BBLUE": "\u001b[34;1m",
    "BMAGENTA": "\u001b[35;1m",
    "BCYAN": "\u001b[36;1m",
    "BWHITE": "\u001b[37;1m"
}

BG_DICT: dict[str, str] = {
    # The first 11 codes are just favorites I picked.
    # Some have short and long names for duplicates.
    # Add more personalized colors by name if desired ...
    "MAIN": "\u001b[48;5;185m",
    "COOL": "\u001b[48;5;38m",
    "MIKES_BLUE": "\u001b[48;5;38m",
    "GO": "\u001b[48;5;28m",
    "GREEN_MEANS_GO": "\u001b[48;5;28m",
    "WARN": "\u001b[48;5;203m",
    "CHERRY": "\u001b[48;5;124m",
    "CANARY": "\u001b[48;5;226m",
    "DANGERWILLROBINSON": "\u001b[48;5;203m",
    "ATTN": "\u001b[48;5;178m",
    "WHATABURGER": "\u001b[48;5;178m",
    "PURPLE": "\u001b[48;5;93m",
    "PURPLEHAZE": "\u001b[48;5;93m",
    "RESET": "\u001b[0m",  # Reset all attributes
    "NEXT_BG": "\u001b[48m",  # Next Background in Cycle (rainbow ...)
    "DEF_BG": "\u001b[49m",  # Reset to Default Background
    # These are the codes for the background 8 color set
    "BG_BLACK": "\u001b[40m",
    "BG_RED": "\u001b[41m",
    "BG_GREEN": "\u001b[42m",
    "BG_BROWN": "\u001b[43m",
    "BG_BLUE": "\u001b[44m",
    "BG_MAGENTA": "\u001b[45m",
    "BG_CYAN": "\u001b[46m",
    "BG_GRAY": "\u001b[47m",
    # These are added to the 8-color BG to make the 16 color BG set
    "BG_BBlack": "\u001b[40;1m",
    "BG_BRed": "\u001b[41;1m",
    "BG_BGreen": "\u001b[42;1m",
    "BG_BYellow": "\u001b[43;1m",
    "BG_BBlue": "\u001b[44;1m",
    "BG_BMagenta": "\u001b[45;1m",
    "BG_BCyan": "\u001b[46;1m",
    "BG_BWhite": "\u001b[47;1m",
}

FLAGS_DICT: dict[str, str] = {
    "RESET": "\u001b[0m",
    "BOLD": "\u001b[1m",
    "DIM": "\u001b[2m",
    "ITALIC": "\u001b[3m",
    "UNDER": "\u001b[4m",
    "REVERSE": "\u001b[7m",
    "CONCEAL": '\u001b[8m'
}


def _generate_ansi256_codes():
    """
    Fill in the 256 set color codes
    """
    #   => (0 to 231) colors in the format 'COLOR133'
    tmp_color_code: int = 0
    for tmp_color_code in range(0, 232):
        FG_DICT["COLOR" + str(tmp_color_code)] = \
            "\u001b[38;5;" + str(tmp_color_code) + "m"
        BG_DICT["COLOR" + str(tmp_color_code)] = \
            "\u001b[48;5;" + str(tmp_color_code) + "m"

    #   => (232 to 255) grayscale in the format 'GRAY243'
    for tmp_color_code in range(232, 256):
        key = "GRAY" + str(tmp_color_code)
        FG_DICT["GRAY" + str(tmp_color_code)] = "\u001b[38;5;" + \
            str(tmp_color_code) + "m"
        BG_DICT["GRAY" + str(tmp_color_code)] = "\u001b[48;5;" + \
            str(tmp_color_code) + "m"


# Turn off color when using ipython, otherwise leave it on
ENABLE_COLOR: bool = True
if py_shell() in ["ipython", "ipython-notebook"]:
    ENABLE_COLOR = False

DEFAULT_FG_COLOR: str = "MAIN"
DEFAULT_BG_COLOR: str = "BG_BLACK"
DEFAULT_FLAGS: str = "RESET"


def color_encode(
        fg_color: str = DEFAULT_FG_COLOR,
        bg_color: str = DEFAULT_BG_COLOR,
        flags_color: str = DEFAULT_FLAGS,
) -> str:
    """ Returns encoded ANSI text string from components.

        Keyword Arguments:
                fg_color {str} - ANSI foreground color {DEFAULT_FG_COLOR}
                bg_color {str} - ANSI background color {DEFAULT_BG_COLOR}
                flags_color {str} - ANSI format codes

        Returns:
            str - printable escaped ANSI text formatting string
        """
    color_code: str = ''
    if ENABLE_COLOR:
        color_code += FG_DICT[fg_color]
        color_code += BG_DICT[bg_color]
        color_code += FLAGS_DICT[flags_color]
    return s


DEFAULT_ENCODE: str = color_encode(
    DEFAULT_FG_COLOR, DEFAULT_BG_COLOR, DEFAULT_FLAGS)
STICKY_ENCODE: str = DEFAULT_ENCODE
# This code will reset all ANSI codes to default.
RESET_ENCODE: str = color_encode(
    DEFAULT_FG_COLOR, DEFAULT_BG_COLOR, DEFAULT_FLAGS)

# *############## Print Functions


def color_print(color_code: str, *args: Any, **kwargs: Any) -> int:
    """ Print using ANSI color codes

        Arguments:
            color_code {str} - printable escaped ANSI text formatting string
            args {tuple} - passthrough for print arguments
            kwargs {dict} - passthrough for print options

        Return:
            int: 0 for success; > 0 for error code """
    try:
        if ENABLE_COLOR:
            print(color_code, *args, STICKY_ENCODE, **kwargs)
        else:
            print(*args, **kwargs)
    except RuntimeError:
        return 1
    return 0


def color_gradient(color_1: int, color_2: int, print_string: str) -> int:
    """ Print <print_string> using a calculated ANSI color gradient
            that changes evenly and gradually between color_1 and color_2.

        Arguments:
            color_1 {int} - ANSI color code(256 set) - lower gradient bound
            color_2 {int} - ANSI color code(256 set) - upper gradient bound
            print_string {str} - target string

        Returns:
            int: 0 for success; > 0 for error code """
    if ENABLE_COLOR and len(print_string) >= 4:
        result: str = ''
        # make sure color_2 is the larger number
        if color_1 > color_2:
            color_1, color_2 = color_2, color_1
        try:
            gradient_slope: float = (color_2 - color_1) / len(print_string)
            for i, _ in enumerate(print_string):
                color_code = "COLOR" + str(int(color_1 + i * gradient_slope))
                result += color_encode(color_code) + print_string[i]
            print(result)
        except TypeError:
            return 1
    return 0


def color_cycle(color_1: int, print_string: str) -> int:
    """ Print by cycling through colors starting at <color_1>.

        Arguments:
            color_1 {int} - ANSI color code(256 set) - lower gradient bound
            print_string {str} - target string

        Returns:
            int: 0 for success; > 0 for error code """
    if ENABLE_COLOR:
        try:
            for _, c in enumerate(print_string):
                color_1 += 1
                if color_1 < 1 or color_1 > 230:
                    color_1 = 1
                color_code = "COLOR" + str(color_1)
                print(color_encode(color_code), str(c), sep="", end="")
            print(DEFAULT_ENCODE, ' ', sep="", end="")
        except (RuntimeError, IndexError):
            return 1
    return 0


def loading(count: int) -> int:
    """ Demo - Print <count> text progress bars.
            They are non responsive and synchronous.

        Arguments:
            count {int} - number of bars

        Returns:
            int: 0 for success; > 0 for error code """
    import time
    import random

    width: int = 0
    w_string: str = ""
    all_progress = [0] * count
    sys.stdout.write("\n" * count)  # space to draw the bars
    while any(x < 100 for x in all_progress):
        time.sleep(0.003)
        # Randomly increment one of our progress values
        unfinished = [(i, v) for (i, v) in enumerate(all_progress) if v < 100]
        index, _ = random.choice(unfinished)
        all_progress[index] += 1
        # Draw the progress bars
        sys.stdout.write(u"\u001b[1000D")  # Move left
        sys.stdout.write(u"\u001b[" + str(count) + "A")  # Move up
        for progress in all_progress:
            width = int(progress / 4)
            w_string = "#" * width
            pad_string = " " * (25 - width)
            if len(w_string) >= 5:
                pad_string = " " * (25 - width)
                pad_string = "|" + w_string + pad_string + "]"
            else:
                pad_string = " " * 21
                pad_string = "|" + w_string + pad_string + "]"
            color_cycle(124, pad_string)
    return 0


def fg_samples():
    """ Foreground color samples """
    i: int = 0
    for k in FG_DICT:
        if i < 32:
            if not i % 8:
                print()
        elif not i % 6:
            print()
        i += 1
        color_print(
            color_encode(k, DEFAULT_BG_COLOR),
            k.replace("OLOR", ""),
            " ",
            sep="",
            end="",
        )
    print()


def bg_samples():
    """ Background color samples """
    i = 0
    for k in BG_DICT:
        if i < 32:
            if not i % 8:
                print()
        elif not i % 6:
            print()
        i += 1
        color_print(
            color_encode(DEFAULT_FG_COLOR, k),
            k.replace("OLOR", ""),
            " ",
            sep="",
            end="",
        )
    print()


def flags_samples():
    """ ANSI Flags samples """
    print()
    i: int = 0
    s: str = 'Now is the time for all good men' + \
        'to come to the aid of their country.'
    for k in FLAGS_DICT:
        i += 1
        color_print(
            color_encode("BWHITE", "PURPLEHAZE", k),
            i,
            " : ",
            str(k),
            "  \t",
            s,
            RESET_ENCODE,
            sep="",
        )
    print()
    color_gradient(
        130,
        144,
        "Gradient!!!  \t{}\n".format(s),
    )
    print()
    color_cycle(
        130,
        "Cycle!!!  \t{}\n".format(s*5)
    )
    print()
    # if ENABLE_COLOR:
    #     loading(5)
    # print()
    color_print(DEFAULT_ENCODE)
    color_print(color_encode("BWHITE", "PURPLEHAZE",
                             "ITALIC"), "TESTS COMPLETE ...")


if __name__ == "__main__":
    # TEST SAMPLES to use if script is run from the command lines

    if len(sys.argv) < 2:
        # color_cycle(42, usage)
        color_gradient(42, 222, USAGE)
    else:
        arg1: str = sys.argv[1].lower()
        if arg1 in ["version", "-v", "--version"]:
            color_cycle(88, VERSION)
        elif arg1 in ["help", "-h", "--help"]:
            color_print(color_encode(
                "BWHITE", "PURPLEHAZE", "ITALIC"), VERSION)
            print()
            color_cycle(88, ANSI_CHART)
        elif arg1 in ["demo", "-d", "--demo"]:
            fg_samples()
            bg_samples()
            flags_samples()
        else:
            color_gradient(42, 222, USAGE)
            # color_cycle(42, usage)

    print("\n\n")
    print("python version (pyver): ", pyver())
    print("python shell (py_shell): ", py_shell())


USAGE: str = (
    """

author    - Michael Treanor  <skeptycal@gmail.com>
copyright - 2019 (c) Michael Treanor
license   - MIT <https://opensource.org/licenses/MIT>
github    - https://www.github.com/skeptycal

Usage: {} {demo|version|help}

  Parameters:
      demo, -d, --demo        -- install and initialize
      version, -v, --version  -- display version information
      help, -h, --help        -- display usage and information
    """.format(os.path.basename(__file__))
)
# Resources:

# https://www.geeksforgeeks.org/print-colors-python-terminal/

# https://stackoverflow.com/questions/287871/print-in-terminal-with-colors
#   1,000,002 ways to do this ... but I still did it my own way ...

# https://en.wikipedia.org/wiki/ANSI_escape_code

# Sequences have different lengths.
#   All sequences start with ESC (27 / hex 0x1B / octal 033), followed
#   by a second byte in the range 0x40 - 0x5F (ASCII @A-Z[\\]^_)
