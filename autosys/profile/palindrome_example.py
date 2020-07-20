# Core Library modules
import operator
import random
import timeit

# Third party modules
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


def is_palindrome_str(x: int) -> bool:
    s = str(x)

    if len(s) == 1:
        palindrome = True

    i = int(len(s) / 2)

    for p in range(i):
        if s[p] != s[-(p + 1)]:
            return False
        else:
            palindrome = True

    return palindrome


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


def generate_palindrome(nb_chars):
    chars = "abcdefghijklmnopqrstuvwxyz"
    prefix = "".join([random.choice(chars) for _ in range(nb_chars)])
    return prefix + prefix[::-1]


def main():
    text = generate_palindrome(nb_chars=1000)
    functions = [
        (is_palindrome_str, "is_palindrome_str"),
        (is_palindrome_dict, "is_palindrome_dict"),
    ]
    functions = functions[::-1]
    duration_list = {}
    for func, name in functions:
        durations = timeit.repeat(lambda: func(text), repeat=1000, number=3)
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


if __name__ == "__main__":
    main()
