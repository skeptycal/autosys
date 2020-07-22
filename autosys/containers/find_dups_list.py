#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' find_dups_list.py - Find duplicates in a list or other sequence.
    Reference: https://www.techiedelight.com/find-duplicates-within-given-range-array/
    '''


def has_duplicates(A, k):
    ''' Returns True if A has duplicates within range k.

        Reference: https://www.techiedelight.com/find-duplicates-within-given-range-array/ '''
    # stores (element, index) pairs as (key, value) pairs
    _dict = {}

    # traverse the list
    for i, e in enumerate(A):

        # if the current element already exists in the dict
        if e in _dict:

            # return true if current element is repeated within range of k
            if i - _dict.get(e) <= k:
                print(_dict)
                return True

        # store elements along with their indices
        _dict[e] = i

    # we reach here when no element is repeated within range k
    return False


def has_duplicates_alt(A, k):
    ''' Returns True if A has duplicates within range k. '''
    # stores (element, index) pairs as (key, value) pairs
    _dict = {}

    # traverse the list
    for i, e in enumerate(A):

        # if the current element already exists in the dict
        if e in _dict:

            # return true if current element is repeated within range of k
            if i - _dict.get(e) <= k:
                print(_dict)
                return True

        # store elements along with their indices
        _dict[e] = i

    # we reach here when no element is repeated within range k
    return False


def example_has_duplicates():
    A = [5, 6, 8, 2, 4, 6, 9]
    k = 4

    if has_duplicates(A, k):
        print("Duplicates found")
    else:
        print("No Duplicates found")


if __name__ == '__main__':
    pass
    example_has_duplicates()
