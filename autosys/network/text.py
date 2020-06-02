# -*- coding: utf-8 -*-
""" Part of the `AutoSys` package
        copyright (c) 2019 Michael Treanor
        https://www.github.com/skeptycal/autosys
        https://www.twitter.com/skeptycal

    `AutoSys` is licensed under the `MIT License
        `<https://opensource.org/licenses/MIT>`
    """
__license__ = "MIT"

# * text messaging
DEFAULT_SCRIPT_PATH: str = os.getcwd() + "/sentMessage.scpt"
DEFAULT_CELL_NUMBER: str = '13616488261'


class Text_Messaging():

    def text(self,
             message: str,
             cell: str = DEFAULT_CELL_NUMBER,
             verbose: bool = False) -> int:
        """ Return status of {message} sent to {cell}(verbose - give CLI feedback if True """
        script_text = "osascript {} {} '{}'".format(DEFAULT_SCRIPT_PATH, cell, message)
        db_print('script_text: ', script_text)
        try:
            result = os.system(script_text)
        except:
            result = -1
        finally:
            db_print('result: ', result)
            return result

    def test_text(self, message: str = 'A python program just sent you a message ...'):
        """ Send a test message using <text> """
        test_cell_number = DEFAULT_CELL_NUMBER
        db_print(f"{message=}")
        result = text(message=message, verbose=SET_DEBUG)
        print(f"{result=}")
