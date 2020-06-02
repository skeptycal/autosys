
import re

# !---------------------------------------------- pre-formatted regex patterns
RE_ALL_NUMS = re.compile(r'[-+]?[\d]*[.]?[\d]+')

# !---------------------------------------------- constants
example_nums = [
    'this is 1 a number 2 lsd23 asdlk;ajsdf8jls.df3409.884-5olksd0.898u-908sdf ',
    'f8f3k4j0.1383jfdfal9'
]


# !---------------------------------------------- search functions


def find_all_numbers(s):
    return re.findall(RE_ALL_NUMS, s)


print(find_all_numbers(example1))

# !---------------------------------------------- dev tests


def _tests_():
    x = find_all_numbers(example1)
    print(x)

# !---------------------------------------------- cli features


def _main_():
    '''
    CLI script main entry point.
    '''
    _debug_: bool = True
    if _debug_:
        _tests_()


if __name__ == "__main__":  # if script is loaded directly from CLI
    _main_()
