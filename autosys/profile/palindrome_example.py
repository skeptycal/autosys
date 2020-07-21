#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Part of the `AutoSys` package
        copyright (c) 2019 Michael Treanor
        https://www.github.com/skeptycal/autosys
        https://www.twitter.com/skeptycal

    `AutoSys` is licensed under the `MIT License
        `<https://opensource.org/licenses/MIT>`
    """

# Nice example from stack overflow
# reference: https://codereview.stackexchange.com/a/245715

# Core Library modules
import operator
import random
import timeit

# Third party modules
import matplotlib.pyplot as plt  # NOQA
import numpy as np
import seaborn as sns  # NOQA


def is_palindrome_str(x: int) -> bool:
    s = str(x)

    if len(s) == 1:
        palindrome = True

    i = int(len(s) / 2)

    for p in range(i):
        if s[p] != s[-(p + 1)]:
            return False
    # this is wrong ... it sets palindrome to True if ANY char matches
    # else:
    #     palindrome = True
    return True


def is_palindrome_str_refactored(x: int) -> bool:
    s = str(x)

    length = len(s)
    if length == 1:
        return True

    # i = int(len(string) / 2) # not sure what this was for ...
    i = length // 2

    for p in range(i):
        if s[p] != s[-(p + 1)]:
            return False

    return True


def is_palindrome_dict(x: int) -> bool:
    s = {i: j for i, j in enumerate(str(x))}
    i = (max(s) + 1) // 2

    if max(s) + 1 == 1:
        return True

    for p in range(i):
        if s[p] != s[max(s) - p]:
            return False
        else:
            palindrome = True

    return palindrome


def quick_check(x: int) -> bool:
    """ A very efficient check to benchmark against. """
    string = str(int)

    length = len(string)
    if length == 1:
        return True

    mid = length // 2

    start = string[:mid]
    finish = string[-mid:]

    # print(f"{start}  ...  {finish}")
    if start == finish:
        return True
    return False


def generate_palindrome(nb_chars):
    chars = "abcdefghijklmnopqrstuvwxyz"
    prefix = "".join([random.choice(chars) for _ in range(nb_chars)])
    mid = random.choice(["", "x"])
    return prefix + mid + prefix[::-1]


def generate_not_palindrome(nb_chars):
    chars = "abcdefghijklmnopqrstuvwxyz"
    prefix = "".join([random.choice(chars) for _ in range(nb_chars)])
    mid = random.choice(["", "x"])
    # these two are intentionally set different and in the middle of the string
    # TODO - could place errors in random locations?
    fudge = "x"
    caramel = "y"
    return prefix + caramel + mid + fudge + prefix[::-1]


def create_boxplot(duration_list):
    plt.figure(num=None, figsize=(8, 4), dpi=300, facecolor="w", edgecolor="k")
    sns.set(style="whitegrid")
    sorted_keys, sorted_vals = zip(
        *sorted(duration_list.items(), key=operator.itemgetter(1))
    )
    flierprops = dict(markerfacecolor="0.75", markersize=1, linestyle="none")
    ax = sns.boxplot(data=sorted_vals, width=0.3, orient="h", flierprops=flierprops,)
    ax.set(xlabel="Time in s", ylabel="")
    plt.yticks(plt.yticks()[0], sorted_keys)
    plt.tight_layout()
    plt.savefig("output.png")


def main():
    string_len = 1000
    n = 100
    repeat = 100

    text = generate_palindrome(nb_chars=string_len)
    not_text = generate_not_palindrome(nb_chars=string_len)
    functions = [
        (is_palindrome_str, "is_palindrome_str"),
        # (is_palindrome_dict, "is_palindrome_dict"),
        (is_palindrome_str_refactored, "is_palindrome_str_refactored"),
        (quick_check, "quick_check"),
    ]
    functions = functions[::-1]
    duration_list = {}

    # palindromes...
    for func, name in functions:

        assert func(text) == False

        durations = timeit.repeat(lambda: func(text), repeat=repeat, number=n)
        duration_list[name] = durations
        print(
            "{func:<20}: "
            "min: {min:0.3f}s, mean: {mean:0.3f}s, max: {max:0.3f}s".format(
                func=name,
                min=min(durations),
                mean=np.mean(durations),
                max=max(durations),
            )
        )

    # non palindromes ...
    for func, name in functions:

        assert func(text) == False
        durations = timeit.repeat(lambda: func(not_text), repeat=repeat, number=n)
        duration_list[name] = durations
        print(
            "{func:<20}: "
            "min: {min:0.3f}s, mean: {mean:0.3f}s, max: {max:0.3f}s".format(
                func=name,
                min=min(durations),
                mean=np.mean(durations),
                max=max(durations),
            )
        )
        create_boxplot(duration_list)


if __name__ == "__main__":
    main()
