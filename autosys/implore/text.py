# -*- coding: utf-8 -*-
""" Part of the `AutoSys` package
        copyright (c) 2019 Michael Treanor
        https://www.github.com/skeptycal/autosys
        https://www.twitter.com/skeptycal

    `AutoSys` is licensed under the `MIT License
        `<https://opensource.org/licenses/MIT>`
    """
__license__ = "MIT"

__all__ = [
    "DEFAULT_SCRIPT_PATH",
    "DEFAULT_CELL_NUMBER",
    "TextMessaging",
    "TextMessagingError",
]

import os

# * text messaging

DEFAULT_SCRIPT_PATH: str = os.getcwd() + "./sentMessage.scpt"
# sendMessage.scpt
DEFAULT_SCRIPT: str = """on run {targetPhoneNumber, targetMessageToSend}
    tell application "Messages"
        set targetService to 1st service whose service type = iMessage
        set targetBuddy to buddy targetPhoneNumber of targetService
        set targetMessage to targetMessageToSend
        send targetMessage to targetBuddy
    end tell
end run"""

DEFAULT_CELL_NUMBER: str = "xxxxxxxxxxx"

with open("cell_number_private.txt", mode="r") as f:
    DEFAULT_CELL_NUMBER: str = f.readline().strip("()-")
    print(DEFAULT_CELL_NUMBER)


class TextMessagingError(Exception):
    pass


class TextMessaging:
    def __init__(
        self, number=DEFAULT_CELL_NUMBER, script_path=DEFAULT_SCRIPT_PATH
    ):
        self.number = number
        self.script_path = script_path

    def text(self, message: str, verbose: bool = False) -> int:
        """ Return status of {message} sent to {cell}(verbose - give CLI feedback if True """
        script_text = "osascript {} {} '{}'".format(
            DEFAULT_SCRIPT_PATH, self.number, message
        )
        db_print("script_text: ", script_text)
        try:
            result = os.system(script_text)
        except:
            result = -1
        finally:
            db_print("result: ", result)
            return result

    def test_text(
        self, message: str = "A python program just sent you a message ..."
    ):
        """ Send a test message using <text> """
        db_print(f"{message=}")
        result = self.text(message=message, verbose=True)
        print(f"{result=}")


tm = TextMessaging()
