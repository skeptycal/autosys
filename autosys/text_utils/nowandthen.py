# from typing import Dict, Final, Tuple
from text_utils.datetime import *
from text_utils.datetime import _check_date_fields, _check_tzinfo_arg


class NowAndThen:
    """ Wrapper for datetime to allow easy access to common functionality. """

    @property
    def now(self):
        return datetime.today()

    @property
    def year(self):
        """ Return current year. """
        return self.now.year

    @property
    def week(self):
        """ Return current month number. """
        return self.now.month

    @property
    def weekday(self):
        """ Return the current weekday. """
        return self.now.strftime("%A")

    def fmt(self, s: str):
        """ Return formatted datetime strings. """
        return self.now.strftime(s)

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


now = NowAndThen()
