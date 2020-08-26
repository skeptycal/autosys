# 'Standard Library'
from dataclasses import dataclass


@dataclass
class AnsiCodes:
    """ ANSI color magic 🦄  """

    # - some favorites
    MAIN: str = "\x1B[38;5;229m"
    WARN: str = "\x1B[38;5;203m"
    BLUE: str = "\x1B[38;5;38m"
    GO: str = "\x1B[38;5;28m"
    CHERRY: str = "\x1B[38;5;124m"
    CANARY: str = "\x1B[38;5;226m"
    ATTN: str = "\x1B[38;5;178m"
    RAIN: str = "\x1B[38;5;93m"
    WHITE: str = "\x1B[37m"
    RESET: str = "\x1B[0m"  # - reset ansi effects
    RESTORE: str = "\x1B[0m"  # - alias of RESET

    # - Encode ANSI 7 bit effect set
    # BOLD: str = "\x1B[1m"
    B: str = "\x1B[1m"
    FAINT: str = "\x1B[2m"
    ITALIC: str = "\x1B[3m"
    IT: str = "\x1B[3m"  # alias of ITALIC
    UNDERLINE: str = "\x1B[4m"
    UL: str = "\x1B[4m"  # alias of UNDERLINE
    BLINK: str = "\x1B[5m"
    REVERSE: str = "\x1B[7m"
    CONCEAL: str = "\x1B[8m"
    STRIKE: str = "\x1B[9m"
    FRAME: str = "\x1B[51m"
    CIRCLE: str = "\x1B[52m"
    OVERLINE: str = "\x1B[53m"

    # - Encode ANSI 7 bit foreground color set
    BLACK: str = "\x1B[30m"
    RED: str = "\x1B[31m"
    GREEN: str = "\x1B[32m"
    YELLOW: str = "\x1B[33m"
    BLUE7: str = "\x1B[34m"  # defined above
    MAGENTA: str = "\x1B[35m"
    CYAN: str = "\x1B[36m"
    # WHITE: str = "\x1B[37m"  # defined above

    # - Encode extended ANSI 7 bit foreground color set
    BRIGHTBLACK: str = "\x1B[30;1m"
    BRIGHTRED: str = "\x1B[31;1m"
    BRIGHTGREEN: str = "\x1B[32;1m"
    BRIGHTYELLOW: str = "\x1B[33;1m"
    BRIGHTBLUE: str = "\x1B[34;1m"
    BRIGHTMAGENTA: str = "\x1B[35;1m"
    BRIGHTCYAN: str = "\x1B[36;1m"
    BRIGHTWHITE: str = "\x1B[37;1m"

    # - Encode ANSI 7 bit background color set
    BBLACK: str = "\x1B[40m"
    BRED: str = "\x1B[41m"
    BGREEN: str = "\x1B[42m"
    BYELLOW: str = "\x1B[43m"
    BBLUE: str = "\x1B[44m"
    BMAGENTA: str = "\x1B[45m"
    BCYAN: str = "\x1B[46m"
    BWHITE: str = "\x1B[47m"

    # - Encode extended ANSI 7 bit background color set
    BBRIGHTBLACK: str = "\x1B[40;1m"
    BBRIGHTRED: str = "\x1B[41;1m"
    BBRIGHTGREEN: str = "\x1B[42;1m"
    BBRIGHTYELLOW: str = "\x1B[43;1m"
    BBRIGHTBLUE: str = "\x1B[44;1m"
    BBRIGHTMAGENTA: str = "\x1B[45;1m"
    BBRIGHTCYAN: str = "\x1B[46;1m"
    BBRIGHTWHITE: str = "\x1B[47;1m"
