from dataclasses import dataclass
from os import linesep as NL
from typing import List

from autosys.profile.autosys_time_it import time_me


@dataclass
class AsciiChars:
    """ #### Newline constants
            NL      - (os.linesep) system specific Newline
            LF      - Linefeed = Linux / macOS Newline
            CR      - Carriage Return
            CRLF    - CR+LF = Windows Newline
            LFCR    - LF+CR = older mac newline code

        #### Common ASCII constants
            NUL     - NUL character
            BEL     - Audible or visual indicator
            BS      - Backspace character
            TAB     - Horizontal Tab character
            VT      - Vertical tab
            FF      - Form Feed (or clear screen)
            ESC     - Escape

        #### Full List

            NUL: str = "\\x00"
            SOH: str = "\\x01"
            STX: str = "\\x02"
            ETX: str = "\\x03"
            EOT: str = "\\x04"
            ENQ: str = "\\x05"
            ACK: str = "\\x06"
            BEL: str = "\\x07"
            BS: str = "\\x08"
            TAB: str = "\\x09"
            VT: str = "\\x0B"
            FF: str = "\\x0C"
            SO: str = "\\x0E"
            SI: str = "\\x0F"
            """

    NL: str = NL
    LF: str = "\x10"
    CR: str = "\x0D"
    CRLF: str = f"{CR}{LF}"
    LFCR: str = f"{LF}{CR}"

    NUL: str = "\x00"
    SOH: str = "\x01"
    STX: str = "\x02"
    ETX: str = "\x03"
    EOT: str = "\x04"
    ENQ: str = "\x05"
    ACK: str = "\x06"
    BEL: str = "\x07"
    BS: str = "\x08"
    TAB: str = "\x09"
    VT: str = "\x0B"
    FF: str = "\x0C"
    SO: str = "\x0E"
    SI: str = "\x0F"

    ESC: str = "\x1B"

    # ASCII control characters
    NUL: str = "\x00"  # Null character
    SOH: str = "\x01"  # Start of Header
    STX: str = "\x02"  # Start of Text
    ETX: str = "\x03"  # End of Text
    EOT: str = "\x04"  # End of Trans.
    ENQ: str = "\x05"  # Enquiry
    ACK: str = "\x06"  # Acknowledgement
    BEL: str = "\x07"  # Bell
    BS: str = "\x08"  # Backspace
    HT: str = "\x09"  # Horizontal Tab
    LF: str = "\x10"  # Line feed
    VT: str = "\x11"  # Vertical Tab
    FF: str = "\x12"  # Form feed
    CR: str = "\x13"  # Carriage return
    SO: str = "\x14"  # Shift Out
    SI: str = "\x15"  # Shift In
    DLE: str = "\x16"  # Data link escape
    DC1: str = "\x17"  # Device control 1
    DC2: str = "\x18"  # Device control 2
    DC3: str = "\x19"  # Device control 3
    DC4: str = "\x20"  # Device control 4
    NAK: str = "\x21"  # Negative acknowl.
    SYN: str = "\x22"  # Synchronous idle
    ETB: str = "\x23"  # End of trans. block
    CAN: str = "\x24"  # Cancel
    EM: str = "\x25"  # End of medium
    SUB: str = "\x26"  # Substitute
    ESC: str = "\x27"  # Escape
    FS: str = "\x28"  # File separator
    GS: str = "\x29"  # Group separator
    RS: str = "\x30"  # Record separator
    US: str = "\x31"  # Unit separator
    DEL: str = "\u0127"  # Delete

    # extended ASCII
    char128: str = "Ç"
    char129: str = "ü"
    char130: str = "é"
    char131: str = "â"
    char132: str = "ä"
    char133: str = "à"
    char134: str = "å"
    char135: str = "ç"
    char136: str = "ê"
    char137: str = "ë"
    char138: str = "è"
    char139: str = "ï"
    char140: str = "î"
    char141: str = "ì"
    char142: str = "Ä"
    char143: str = "Å"
    char144: str = "É"
    char145: str = "æ"
    char146: str = "Æ"
    char147: str = "ô"
    char148: str = "ö"
    char149: str = "ò"
    char150: str = "û"
    char151: str = "ù"
    char152: str = "ÿ"
    char153: str = "Ö"
    char154: str = "Ü"
    char155: str = "¢"
    char156: str = "£"
    char157: str = "¥"
    char158: str = "₧"
    char159: str = "ƒ"
    char160: str = "á"
    char161: str = "í"
    char162: str = "ó"
    char163: str = "ú"
    char164: str = "ñ"
    char165: str = "Ñ"
    char166: str = "ª"
    char167: str = "º"
    char168: str = "¿"
    char169: str = "⌐"
    char170: str = "¬"
    char171: str = "½"
    char172: str = "¼"
    char173: str = "¡"
    char174: str = "«"
    char175: str = "»"
    char176: str = "░"
    char177: str = "▒"
    char178: str = "▓"
    char179: str = "│"
    char180: str = "┤"
    char181: str = "╡"
    char182: str = "╢"
    char183: str = "╖"
    char184: str = "╕"
    char185: str = "╣"
    char186: str = "║"
    char187: str = "╗"
    char188: str = "╝"
    char189: str = "╜"
    char190: str = "╛"
    char191: str = "┐"
    char192: str = "└"
    char193: str = "┴"
    char194: str = "┬"
    char195: str = "├"
    char196: str = "─"
    char197: str = "┼"
    char198: str = "╞"
    char199: str = "╟"
    char200: str = "╚"
    char201: str = "╔"
    char202: str = "╩"
    char203: str = "╦"
    char204: str = "╠"
    char205: str = "═"
    char206: str = "╬"
    char207: str = "╧"
    char208: str = "╨"
    char209: str = "╤"
    char210: str = "╥"
    char211: str = "╙"
    char212: str = "╘"
    char213: str = "╒"
    char214: str = "╓"
    char215: str = "╫"
    char216: str = "╪"
    char217: str = "┘"
    char218: str = "┌"
    char219: str = "█"
    char220: str = "▄"
    char221: str = "▌"
    char222: str = "▐"
    char223: str = "▀"
    char224: str = "α"
    char225: str = "ß"
    char226: str = "Γ"
    char227: str = "π"
    char228: str = "Σ"
    char229: str = "σ"
    char230: str = "µ"
    char231: str = "τ"
    char232: str = "Φ"
    char233: str = "Θ"
    char234: str = "Ω"
    char235: str = "δ"
    char236: str = "∞"
    char237: str = "φ"
    char238: str = "ε"
    char239: str = "∩"
    char240: str = "≡"
    char241: str = "±"
    char242: str = "≥"
    char243: str = "≤"
    char244: str = "⌠"
    char245: str = "⌡"
    char246: str = "÷"
    char247: str = "≈"
    char248: str = "°"
    char249: str = "∙"
    char250: str = "·"
    char251: str = "√"
    char252: str = "ⁿ"
    char253: str = "²"
    char254: str = "■"
    char255: str = "  	"


def char(i: int) -> (str):
    """ Return a printable character from the 'chr' function. """

    try:
        retval = int(i)
        retval = chr(i)
        return retval if len(retval) else " "
    except:
        return " "


def __fmt_def(i: int) -> (str):
    return f"{chr(i)}: str = '{chr(i)}' # ascii code {i} {hex(i)}h"


def __ascii_definition_list(a: int, b: int) -> (List[str]):
    return [__fmt_def(i) for i in range(a, b)]


def __generate_ascii():
    for i in range(32, 127):
        print()


def _test_f1(i=185, n=50000):
    for i in range(n):
        _ = __fmt_def(i)


if __name__ == "__main__":
    from dis import dis

    print("Test ascii generator and class functions:")
    f = __fmt_def
    dis(f)

    ascii_code: int = 1
    while True:
        print(f(ascii_code))
        ascii_code += 1
        if ascii_code > 40:
            break

# __generate_ascii()
# print(__ascii_definition_list(32, 127))
