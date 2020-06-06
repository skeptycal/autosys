from dataclasses import dataclass
from os import linesep as NL
from typing import Dict, Final, Tuple
from autosys.text_utils.datetime import *

from autosys.text_utils.datetime import datetime as dt
from autosys.text_utils.datetime import _check_date_fields, _check_tzinfo_arg


class NowAndThenError(Exception):
    """ An error in the NowAndThen datetime processing has occurred. """


@dataclass
class NowAndThen(dt):
    """ Partial wrapper for datetime to allow easy access to current
        information.

        (Methods calls are based on 'datetime.today()')

        common types from 'datetime':
            date, time, datetime (all are immutable and hashable)

        common methods, etc from 'datetime':
            basic:          date, time, now, today
            detailed:       hour, minute, second, month, day, year, weekday
            formatting:     strftime, strptime, timestamp, timetuple

        All objects are assumed to be tz naive for this implementation,
        but the method 'is_aware' was added to check as needed.
    """

    def is_aware(self, obj: (datetime, datetime.time)) -> (bool, None):
        """ Return True if an object is tz 'aware' or False if 'naive'.
            (All other objects will report an error.)

            obj = a 'datetime' or 'time' object

            (Date and time objects may be categorized as “aware” or “naive”
            depending on whether or not they include timezone information.)
            """
        if isinstance(obj, datetime):
            return obj.tzinfo is not None and obj.tzinfo.utcoffset(obj) is not None
        if isinstance(obj, datetime.time):
            return obj.tzinfo is not None and obj.tzinfo.utcoffset(None) is not None
        raise NowAndThenError(
            f"The object '{obj}' is not capable of time zone awareness"
        )

    def __getattribute__(self, name):
        return self.today().__getattribute__(name)

    def get_copyright_date(
        self, start_year: int = 0, _author: str = "", symbol: str = "(c)",
    ) -> (str):
        """ Return a correct formatted copyright string. """
        try:  # if start year is not an integer, fix it
            start_year = int(start_year)
        except:
            start_year = self.year

        if 1900 < start_year < self.year:  # is start year in (1900-now)?
            return f"Copyright {symbol} {start_year}-{self.year} {_author}"
        else:
            start_year = self.year
            return f"Copyright {symbol} {self.year} {_author}"


now = NowAndThen

# print(now())
print(now.date)
print(now.time)
# print(now.week())


def guts(obj=None):
    return obj. + ", ".join(_ for _ in dir(obj) if not _.startswith("_"))


def help(obj=None):
    return obj.__doc__


def p(obj):
    print(guts(obj=obj))


print()
p(0)
