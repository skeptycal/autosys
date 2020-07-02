#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Prints today's date
# 'Standard Library'
from datetime import date, datetime, time

# 'package imports'
from autosys.cli.debug import br, dbprint, hr

# Days start at 0 for monday
days = [
    "monday",
    "tuesday",
    "wednesday",
    "thursday",
    "friday",
    "saturday",
    "sunday",
]


class int_restricted(int):
    pass


class DT(datetime):
    def __init__(self):
        self.dt = datetime.now()

    @property
    def today(self):
        return self.dt.today()

    @property
    def now(self):
        return f"{self.today:%H:%M %p}"

    def __str__(self):
        return f"{self.today:%B %d, %Y}"


def main():
    # DATETIME OBJECTS
    # Get today's date from datetime class
    today = datetime.now()
    print(today)
    # Get the current time
    t = datetime.time(datetime.now())
    print("The current time is", t)
    # weekday returns 0 (monday) through 6 (sunday)
    wd = date.weekday(today)

    print("Today is day number %d" % wd)
    print("which is a " + days[wd])

    print()
    # instance of DT class for testing
    dt = DT()

    print(bool.__bases__)
    print(f"{dt=}")
    print(f"dt: {dt}")
    br()
    print(f"{dt.today=}")
    print(dt.now)
    print(f"{dt.today:%B %d, %Y}")


if __name__ == "__main__":
    main()
