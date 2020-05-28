# from typing import Dict, Final, Tuple
from autosys.text_utils.datetime import *
from autosys.text_utils.datetime import _check_date_fields, _check_tzinfo_arg


class NowAndThen(datetime):
    """ Wrapper for datetime to allow easy access to common functionality. """

    def __init__(self):
        pass

    def __new__(
        cls,
        year=None,
        month=None,
        day=None,
        hour=0,
        minute=0,
        second=0,
        microsecond=0,
        tzinfo=None,
        *,
        fold=0,
    ):
        if (
            isinstance(year, (bytes, str))
            and len(year) == 10
            and 1 <= ord(year[2:3]) & 0x7F <= 12
        ):
            # Pickle support
            if isinstance(year, str):
                try:
                    year = bytes(year, "latin1")
                except UnicodeEncodeError:
                    # More informative error message.
                    raise ValueError(
                        "Failed to encode latin1 string when unpickling "
                        "a datetime object. "
                        "pickle.load(data, encoding='latin1') is assumed."
                    )
            self = object.__new__(cls)
            self.__setstate(year, month)
            self._hashcode = -1
            return self
        year, month, day = _check_date_fields(year, month, day)
        hour, minute, second, microsecond, fold = _check_time_fields(
            hour, minute, second, microsecond, fold
        )
        _check_tzinfo_arg(tzinfo)
        self = object.__new__(cls)
        self._year = year
        self._month = month
        self._day = day
        self._hour = hour
        self._minute = minute
        self._second = second
        self._microsecond = microsecond
        self._tzinfo = tzinfo
        self._hashcode = -1
        self._fold = fold
        return self

    # @property
    # def year(self):
    #     """ Return current year. """
    #     return datetime.today().year

    # @property
    # def now(self):
    #     return datetime.today()

    # @property
    # def week(self):
    #     """ Return current month number. """
    #     return datetime.today().month

    # @property
    # def weekday(self):
    #     """ Return the current weekday. """
    #     return datetime.today().strftime("%A")

    # def fmt(self, s: str):
    #     """ Return formatted datetime strings. """
    #     return datetime.today().strftime(s)

    # def __getattribute__(self, name):

    #     datetime.today().
    #     if hasattr(datetime.today(), name):
    #         print(f"__getattribute__ succeeded with name {name}")
    #         print(f"The response was {datetime.today().__getattribute__(name)}")
    #         return datetime.today().__getattribute__(name)
    #     else:
    #         print(f"  __getattribute__ failed with name {name}")
    #         return datetime.now()
    #         # try:
    #         #     return f"datetime.today().{name}"
    #         # except:
    #         #     return datetime.today().now()
    #     # else:
    #     #     return self.get(name)

    def get_copyright_date(
        self, start_year: int = 0, _author: str = "", symbol: str = "(c)",
    ) -> str:
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

if __name__ == "__main__":
    print(now().year)
