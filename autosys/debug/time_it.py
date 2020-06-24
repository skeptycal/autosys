#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import json
from collections import deque
from dataclasses import dataclass, field, Field
from functools import lru_cache
from os import linesep as NL
from time import perf_counter_ns as timer
from typing import Deque, Dict, List, Tuple

time_list = []

log = logging.getLogger(__file__)


class TimeItError(Exception):
    pass


class TimerDeque(deque):
    def __init__(self, iterable, maxlen, flush=False):
        self.flush = flush
        super().__init__(iterable, maxlen)

    def _log(self):
        log.info(NL.join(self))
        json.dump(obj=self, fp='time_it.json')

    def append(self, x):
        if self.flush:
            if len(self) > self.maxlen:
                self._log()
                self.clear()
        return super().append(x)


@dataclass
class TimeIt:
    reps: int = 100
    history_size: int = 32768
    save_on_full: bool = False
    get_kw: bool = True
    cli_output: bool = True
    log_output: bool = True
    # _units: int = field(default=0, init=False)
    time_list: Field = field(init=False)
    UNIT_DICT: Field = field(init=False)
    DEFAULT_TARGET_FORMAT: str = (5, 3)

    def __post_init__(self):
        ''' Parameter Setup:

            _units - unit multiplier in use for this timer instance

            time_list - a timer log of time measurements in a deque of size <history_size>

            history_size - number of entries stored in the <time_list> timer log

            save_on_full - a flag to decide if the timer log should be written to a logfile when it is filled and the log cleared

            UNIT_DICT - a dict of allowed time unit multipliers along with other info (assuming the perf_counter_ns is used so times are initially reported in integer ns)
            '''
        self.time_list: TimerDeque[str] = TimerDeque(
            [], maxlen=self.history_size, flush=self.save_on_full)
        self.UNIT_DICT: Dict[int, Tuple] = {
            0: ('nanoseconds', 'ns', 10**0),
            3: ('microseconds', 'µs', 10**3),
            6: ('milliseconds', 'ms', 10**6),
            9: ('seconds', 's', 10**9),
        }
        self._n = self.reps
        self.dt = 0
        self._unit_index: int = 0
        if self._n < 5 or self._n > 2000:
            self._n = 100

    @property
    def key_by_index(self):
        ''' Return the key for the current unit index. '''
        try:
            return self.keys[self._unit_index]
        except KeyError:
            raise TimeItError(
                f'The unit dictionary does not contain a key at index {self._unit_index}')

    @property
    def keys(self):
        ''' Return keys from the unit dictionary. '''
        return tuple(self.UNIT_DICT.keys())

    @property
    def _unit_data(self):
        ''' Return tuple containing unit information for the current unit. '''
        try:
            return self.UNIT_DICT[self.key_by_index]
        except KeyError:
            raise TimeItError(
                f'The unit dictionary does not contain the key {self.key_by_index}')

    @property
    def unit_name(self):
        ''' Return unit name. '''
        try:
            return self._unit_data[0]
        except:
            raise TimeItError(
                f'The unit name at index 0 could not be found.')

    @property
    def unit(self):
        ''' Return unit abbreviation. '''
        try:
            return self._unit_data[1]
        except:
            raise TimeItError(
                f'The unit abbreviation at index 1 could not be found.')

    @property
    def unit_multiplier(self):
        ''' Return unit multiplier. '''
        try:
            return self._unit_data[2]
        except:
            raise TimeItError(
                f'The unit multiplier at index 2 could not be found.')

    @property
    def avg(self):
        ''' Return current time average.

            (total ∆t / number of trials)
            '''

        try:
            return self.dt / self._n
        except:
            raise TimeItError(
                f'There was a error calculating the average ({self.dt} / {self._n}).')

    @property
    def scale(self):
        ''' Return scaled time based on unit multiplier. '''
        try:
            return self.dt / self.unit_multiplier
        except:
            raise TimeItError(
                f'There was a error scaling the time ({self.dt} / {self.unit_multiplier}).')

    @property
    def n(self):
        return self._n

    def _log(self, name):
        ''' Log data to stdout and/or log file. '''
        tf = f"{name}\n avg: {self.avg} {self.unit} (n={self._n})"
        if self.cli_output:
            print(tf)
            print()
        if self.log_output:
            self.time_list.append(tf)

    def timeit(self, method):
        ''' Decorator to time method code execution.
            ---

            Code will be repeated n times and the method name and time are sent to the _log function before the normal return value is returned.

            An appropriate unit and n are chosen based on example tests.

            '''
        # TODO - add a toggle for @lru_cache
        # @lru_cache
        def timed(*args, **kw):
            self.dt = -timer()
            i: int = 0
            while i < self._n:
                result = method(*args, **kw)
                i += 1
            self.dt += timer()
            kw_arg = f"{args}{kw}" if self.get_kw else ''
            self._log(name=f"{method.__name__}{kw_arg} = {result}")
            return result
        return timed


t = TimeIt(reps=400)

reps = 20
# print(t)
print('-'*40)
print()


@t.timeit
@lru_cache
def time_range_example(reps):
    f = 1
    for i in range(reps):
        f += i
    return f


# print(time_range_example(reps=2))
# print(time_range_example(reps=20))
time_range_example(reps=50)
time_range_example(reps=120)
time_range_example(reps=1200)
# print(time_range_example(reps=12000))
# print(time_range_example(reps=120000))
# print(time_range_example(reps=1200000))
# print(time_range_example(reps=12000000))
