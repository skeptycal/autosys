#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Part of the `AutoSys` package
        copyright (c) 2019 Michael Treanor
        https://www.github.com/skeptycal/autosys
        https://www.twitter.com/skeptycal

    `AutoSys` is licensed under the `MIT License
        `<https://opensource.org/licenses/MIT>`
    """
# watching "Arrays vs Linked Lists - Computerphile"

# what about an array of linked elements?
# it is really a linked list, but will it have some advantages
#   of an array?

# during downtime they are copied back into array format
#   i.e. like memories, when they are sleeping, they are reorganized ...

# during busy times, inserting and removing creates either an extra
#   pointer to new elements or a temporary 'hole' element
#   the 'hole' elements are simply a 'nul' object that would
#   be automatically skipped

# this would be especially good when eleents are sometimes deleted
#   but rarely added

# if new elements are added often, this will struggle

import time
import autosys.lister

# profile with clock ticks as units ...


class Node:
    def __init__(self, data, next_element=None):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null


class DoubleNode(Node):
    def __init__(self, data, prev_element=Element.last, next_element=None):
        super.__init__(self, data=data, next_element=next_element)
        self.last = prev_element  # maybe?


class CircularNode(DoubleNode):
    def __init__(self, data, prev_element=Element.last, next_element=None, head=None):
        super.__init__(self, data, prev_element=prev_element,
                       next_element=next_element)
        self.next = head  # if not head: self.next = None


class LinkedList:
    """
    The class constructor needs to make sure there is a 'first' element,
        track the final element, and initialize new elements with the 
        'last' as 'previous' and 'next' of 'last' as the new one. The
        'next' of new is null.
    """

    def __init__(self):
        self.head = None
        self.index = []  # TODO - just for testing ...

    # This function prints contents of linked list
    # starting from head

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data, end=', ')
            temp = temp.next

    def append(self, node):
        pass

    def insert(self, node):
        pass

    def delete(self, node):
        pass


class DoubleLinkedList(LinkedList):
    pass


class CircularLinkedList(LinkedList):
    pass


# ------------------------------------------------------------------
# watching "Sorting Secret - Computerphile"

# The visual of the 'sorting box' is interesting ...

# what if we just subtract one from the other, e.g.


util = autosys.lister.Lister([])


def sort_subtract(a, b):
    diff = a - b  # this is the difference ... does this help?
    if diff > 0:
        return (b, a)
    return (a, b)


def sort_compare(a, b):
    if a > b:
        return (b, a)
    return (a, b)


# gradient indexing ... downtime maintaining a 'weighted average' index

# e.g. - with example data:
#   AAABCDEEEEEEEEFFFFFFFFGHIJKLLLLMMMMMMMMMMNNNNOPQRSSSSSSSSSSTTTTTTTTTUVWXYZ


def sort_ins(input_list):  # standard iterable or generator
    for x in input_list:
        pass


# builtins ...
def sort_numbers_in_place(input_list, case_sens=True):
    if case_sens:
        input_list = map(lower(), input_list)
        # map(lambda x: x.lower(), ["A", "B", "C"])
    return input_list.sort(reversed=False)


def sort_str_with_lowe(input_list, case_sens=True, rev_case=False, reverse=False):
    if case_sens:
        pass  # just sort it ...


def sort_str_in_parts(input_list, case_sens=True, rev_case=False, reverse=False):
    if case_sens:
        pass  # create 2 lists (upper, lower) and sort before recombining them


def sort_numbers_new_list(input_list):
    return sorted(input_list, reverse=False)


def call_all_sorts(test_lists):
    for L in test_lists:
        pass


test_lists = []
test_lists.append([5, 3, 2, 1, 4])
test_lists.append(['H', 'j', 'A', 'A', 'b', 'x', 'X'])
test_lists.append(['H', 'j', 'A', 'A', 'b', 'x', 'X', ' '])
test_lists.append(['H', 'j', 'A', 'A', 'b', 'x', 'X', ''])
test_lists.append([5, 3, 2, 1, 4])
test_lists.append([5, 3, 2, 1, 4])
test_lists.append([5, 3, 2, 1, 4])


call_all_sorts(test_lists)


# using islower and isupper, paired with the format that is 'usual' for the
# data, will speed up the operation significantly
# https://www.dotnetperls.com/lower-python

def test_is_lower():
    """
    1384626116.650
    1384626122.033    lower():               5.38 s
    1384626124.027    islower() and lower(): 1.99 s
    """
    import time

    value = "intuitive"

    print(time.time())

    # Version 1: lower.
    i = 0
    while i < 10000000:
        v = value.lower()
        i += 1

    print(time.time())

    # Version 2: islower and lower.
    i = 0
    while i < 10000000:
        if not value.islower():
            v = value.lower()
        i += 1

    print(time.time())


test_is_lower()
