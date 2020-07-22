# Profiling examples


# List.reverse()
# vs
# List[::-1]

# dict.get
# vs
# dict[""]

# finding factors:
# for i in range(1, f + 1):
#   if f % i == 0:


# finding memory usage:
# sys.getsizeof()
# vs
# memoryview
# vs
# memory stream


# clear screen
# def screen_clear():
#    # for mac and linux(here, os.name is 'posix')
#    if os.name == 'posix':
#       _ = os.system('clear')
#    else:
#       # for windows platfrom
#       _ = os.system('cls')
#    # print out some text
# vs
# terminal CSI commands
