#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Part of the `AutoSys` package - utilities for macOS apps
        copyright (c) 2019 Michael Treanor
        https://www.github.com/skeptycal/autosys
        https://www.twitter.com/skeptycal

    `AutoSys` is licensed under the `MIT License
        `<https://opensource.org/licenses/MIT>`
    """

""" #TODO -- ideas for maze solver

    - mazes with multiple solutions
    - find shortest
    - find lowest cost
    - make some color coded (or gradients) that label the 'cost' of traversing over a certain area
    - create a 3d maze
    - create an automated way of testing 'solver' algorithms

    """

if True:
    import numpy as np
    import pandas as PD
    from sys import stdout, stderr
    from typing import Dict, List


def indent(*args, **kwargs):
    print("  ", *args, **kwargs)


def eprint(*args, **kwargs):
    """ Print to sys.stderr for debugging. """
    print(*args, file=stderr)


def stats(x):
    """ Print common variable stats to <stderr> for debugging. """
    for i in (_ for _ in dir(x) if not _.startswith("_")):
        print("-" * 50)
        print(i)
        indent(type(dt))
        indent(eval("x." + str(i) + ""))
        indent(eval("type(x." + str(i) + ")"))
        print()


# class Location():
#     """ Location in a 3d space. """

#     def __init__(self, x: int = 0, y: int = 0, z: int = 0):
#         if x:
#             self.x: int = x
#         if y:
#             self.y: int = y
#         if z:
#             self.z: int = z


location = np.dtype(">i4")
dt = np.dtype(">i4")
stats(dt)


class Particle:
    """ #### Model of the properties of a location in 3d space. Some people
        may choose to think of it as a 'particle' of matter.

        data: unspecified type -- data for the properties of Particle

        properties: dict -- additional properties

        Base class for 3d physics models with physical properties and
        arbitrary granular precision.

        Examples of custom properties that could be added are:
        - density
        - temperature
        - 'squishyness'
        - velocity
        - charge
        - Energy
        - material (possibly a class with its own properties)
        """

    def __init__(self, data, properties: Dict, x=0, y=0, z=0):
        super().__init__(data, x=x, y=y, z=z)
        self.props = properties

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class Mass:
    """ A collection of particles in 3d space.

        The properties are determined by the subclass of the <Location> class.
        """

    pass


class Area:
    """ A special subclass of <Mass> that ignores the z-axis by default.
    """

    pass


class Traveler:
    active: bool  # TODO or <done: bool> ???
    location: int


class Maze(Area):
    """ Maze solver

        Reference: based on Computerphile maze solver video.
        """

    start: (0, 5)  # this should be the top center of the maze

    crew: List[
        Traveler
    ] = []  # my crew of travelers who will go out and search the wastelands for a path to the water source

    def make_traveler(self, loc):
        self.crew.append(traveler(loc))

    def start_solving(self):
        make_traveler(START)
