#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Quick Colors

    Make adding color to terminal output as simple as possible. Use quick, short tags in place of Colorama variables. Resembles basic html tags.
    Includes a simple parser to do the tag replacement and automatic string processing.

    ```
    p = QuickColor('')

    p.rint('<r>red <b>blue')

    r = '<R>'
    y = '<y>'

    p.rint(f'{r}red {y}yellow')

    p = QuickColor(f'{r}red {y}yellow')

    print(p)

    color_list = ['<c>', 'cyan ', '<g>', 'green']
    p.rint(color_list)

    ```

    The 'quick print' codes are inline string literals that are similar to html tags and are used as placeholders for automatic replacement with ansi color strings similar to those used by the Pypi package Colorama.


    ```
    # standard colors
    <K>  or  <k>    # K is black
    <B>  or  <b>    # Blue
    <C>  or  <c>    # Cyan
    <G>  or  <g>    # Green
    <M>  or  <m>    # Magenta
    <R>  or  <r>    # Red
    <W>  or  <w>    # White
    <Y>  or  <y>    # Yellow

    # light colors
    <LK> or <lk>    # light black
    <LB> or <lb>    # light Blue
    <LC> or <lc>    # light Cyan
    <LG> or <lg>    # light Green
    <LM> or <lm>    # light Magenta
    <LR> or <lr>    # light Red
    <LW> or <lw>    # light White
    <LY> or <ly>    # light Yellow

    <x> or <X>    # X is for reset
    ```

    They may be upper or lower case. If <reset_color> is set to true (the default), a trailing 'reset' code is automatically added to eliminate color bleeding to upcoming lines.

    Common available methods and attributes:
    ```
    # instantiate
    p = QuickColor('')

    # parse the current string (or new string <s>) and return it
    p.parse(s='optional sequence')

    # print the current string (or new string <s>)
    p.rint(s='optional sequence')

    # visual test of current terminal configuration
    p.test(s='optional values')

    ```


    More info about [Colorama][4]
    ---
    Part of the [AutoSys][1] package

    Copyright (c) 2018 [Michael Treanor][2]

    AutoSys is licensed under the [MIT License][3]

    [1]: https://www.github.com/skeptycal/autosys
    [2]: https://www.twitter.com/skeptycal
    [3]: https://opensource.org/licenses/MIT
    [4]: https://pypi.org/project/colorama/
    """

from dataclasses import Field, dataclass, field
from io import TextIOWrapper
from os import linesep as NL
from sys import stdout

from typing import Dict, Final, List, Sequence


@dataclass
class QuickColor:
    ''' Quick Colors

        Make adding color to terminal output as simple as possible. Use quick, short tags in place of Colorama variables. Resembles basic html tags.
        Includes a simple parser to do the tag replacement and automatic string processing.

        ```
        p = QuickColor('')

        p.rint('<r>red <b>blue')

        r = '<R>'
        y = '<y>'

        p.rint(f'{r}red {y}yellow')

        p = QuickColor(f'{r}red {y}yellow')

        print(p)

        color_list = ['<c>', 'cyan ', '<g>', 'green']
        p.rint(color_list)

        ```

        The 'quick print' codes are inline string literals that are similar to html tags and are used as placeholders for automatic replacement with ansi color strings similar to those used by the Pypi package Colorama.


        ```
        # standard colors
        <K>  or  <k>    # K is black
        <B>  or  <b>    # Blue
        <C>  or  <c>    # Cyan
        <G>  or  <g>    # Green
        <M>  or  <m>    # Magenta
        <R>  or  <r>    # Red
        <W>  or  <w>    # White
        <Y>  or  <y>    # Yellow

        # light colors
        <LK> or <lk>    # light black
        <LB> or <lb>    # light Blue
        <LC> or <lc>    # light Cyan
        <LG> or <lg>    # light Green
        <LM> or <lm>    # light Magenta
        <LR> or <lr>    # light Red
        <LW> or <lw>    # light White
        <LY> or <ly>    # light Yellow

        <x> or <X>    # X is for reset
        ```

        They may be upper or lower case. If <reset_color> is set to true (the default), a trailing 'reset' code is automatically added to eliminate color bleeding to upcoming lines.

        Common available methods and attributes:
        ```
        # instantiate
        p = QuickColor('')

        # parse the current string (or new string <s>) and return it
        p.parse(s='optional sequence')

        # print the current string (or new string <s>)
        p.rint(s='optional sequence')

        # visual test of current terminal configuration
        p.test(s='optional values')

        ```

        '''
    args: Sequence[str]  # Initial arguments passed in as any Sequence type

    reset_color: Final[bool] = True  # True => reset colors at end of line
    RESET_ALL: Final[str] = '\x1b[0m'  # Code to use for reset

    # Print function default keyword arguments
    sep: Final[str] = ''  # not implemented
    end: Final[str] = NL
    file: Final[TextIOWrapper] = stdout
    flush: Final[bool] = False

    # container for current parsed string
    _string: str = ''
    # container for current prepared endline reset string
    _reset: str = ''
    # dictionary of color codes for parsing
    _quick_colors_dict: Dict[str, str] = field(init=False, hash=True)
    # regex pattern for locating tags (not currently implemented)
    # _RE_QUICK_COLOR_TAG: Final[re.Pattern] = re.compile(r'<\w{1,2}>')

    def __post_init__(self):
        ''' Finish configuration of the class instance by filling the
            color dictionary and parsing the initial <args> argument.
            '''
        self._quick_colors_dict = self._get_dict()
        self._string = self.parse(self.args)
        self._reset = self.RESET_ALL * self.reset_color

    def __str__(self):
        ''' Return the a parsed string representing the current value
            of the instance string storage variable.

            To return a parsed string with a new value, use the 'parse'
            method and pass in a new string <s>.'''
        return self.parse()

    def _get_dict(self):
        return {
            '<K>': '\x1b[30m',  # K is black
            '<B>': '\x1b[34m',  # Blue
            '<C>': '\x1b[36m',  # Cyan
            '<G>': '\x1b[32m',  # Green
            '<M>': '\x1b[35m',  # Magenta
            '<R>': '\x1b[31m',  # Red
            '<W>': '\x1b[37m',  # White
            '<Y>': '\x1b[33m',  # Yellow
            '<LK>': '\x1b[90m',  # light colors
            '<LB>': '\x1b[94m',
            '<LC>': '\x1b[96m',
            '<LG>': '\x1b[92m',
            '<LM>': '\x1b[95m',
            '<LR>': '\x1b[91m',
            '<LW>': '\x1b[97m',
            '<LY>': '\x1b[93m',
            '<X>': '\x1b[39m',  # X is for reset
        }

    def parse(self, s: Sequence = ''):
        ''' Return a colorized string ready to print or use. '''
        if s:
            if isinstance(s, str):
                self._string = s
            else:
                self._string = ''.join(s)
        else:
            if not self._string:
                self._string = ''.join(self.args)
        for k, v in self._quick_colors_dict.items():
            self._string = self._string.replace(k, v)
            k = k.lower()
            self._string = self._string.replace(k, v)
        return f"{self._string}{self._reset}"

    def rint(self, s: Sequence = ''):
        ''' Print a parsed string using the QuickColor options
            <end>, <file>, <flush> as print keyword arguments.

            A new string can optionally be passed in as <s> so a single
            class instance can be reused, saving resources.
            '''
        print(self.parse(s=s), end=self.end,
              file=self.file, flush=self.flush)

    def test(self, s: Sequence = ''):
        ''' Assorted visual tests. Use <s> to send in more. '''
        print('QuickColor Tests: ')
        if s:
            self.rint(s=s)
        red = '<r>'
        blue = '<b>'
        color_test = f"<r>red <b>blue"
        print('First test string: ', color_test, ' => ', p.parse(color_test))
        self.rint('<m>magenta <lg>light green')
        r = '<R>'
        y = '<y>'
        self.rint(f'{r}red {y}yellow')
        color_list = ['<c>', 'cyan ', '<g>', 'green']
        self.rint(color_list)


p = QuickColor('')
# p.test()

''' References ...

    Colorama Color Constants are:
        - Fore: BLACK, RED, GREEN, YELLOW, BLUE,
        MAGENTA, CYAN, WHITE, RESET.
        - Back: BLACK, RED, GREEN, YELLOW, BLUE,
        MAGENTA, CYAN, WHITE, RESET.
        - Style: DIM, NORMAL, BRIGHT, RESET_ALL

    colorama_Fore: Dict[str, str] = {
        'BLACK': '\x1b[30m',
        'BLUE': '\x1b[34m',
        'CYAN': '\x1b[36m',
        'GREEN': '\x1b[32m',
        'LIGHTBLACK_EX': '\x1b[90m',
        'LIGHTBLUE_EX': '\x1b[94m',
        'LIGHTCYAN_EX': '\x1b[96m',
        'LIGHTGREEN_EX': '\x1b[92m',
        'LIGHTMAGENTA_EX': '\x1b[95m',
        'LIGHTRED_EX': '\x1b[91m',
        'LIGHTWHITE_EX': '\x1b[97m',
        'LIGHTYELLOW_EX': '\x1b[93m',
        'MAGENTA': '\x1b[35m',
        'RED': '\x1b[31m',
        'RESET': '\x1b[39m',
        'WHITE': '\x1b[37m',
        'YELLOW': '\x1b[33m',
    }
    colorama_Back: Dict[str, str] = {
        'BLACK': '\x1b[40m',
        'BLUE': '\x1b[44m',
        'CYAN': '\x1b[46m',
        'GREEN': '\x1b[42m',
        'LIGHTBLACK_EX': '\x1b[100m',
        'LIGHTBLUE_EX': '\x1b[104m',
        'LIGHTCYAN_EX': '\x1b[106m',
        'LIGHTGREEN_EX': '\x1b[102m',
        'LIGHTMAGENTA_EX': '\x1b[105m',
        'LIGHTRED_EX': '\x1b[101m',
        'LIGHTWHITE_EX': '\x1b[107m',
        'LIGHTYELLOW_EX': '\x1b[103m',
        'MAGENTA': '\x1b[45m',
        'RED': '\x1b[41m',
        'RESET': '\x1b[49m',
        'WHITE': '\x1b[47m',
        'YELLOW': '\x1b[43m'
    }
    colorama_Style: Dict[str, str] = {
        'BRIGHT': '\x1b[1m',
        'DIM': '\x1b[2m',
        'NORMAL': '\x1b[22m',
        'RESET_ALL': '\x1b[0m'
    }
    '''
