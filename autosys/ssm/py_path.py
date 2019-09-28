
import os
import sys


def print_os_path(arg):
    """ Print path list in newline 'list' format. """
    import os
    print(*arg.split(os.pathsep), sep=os.linesep)


assert(s

print_os_path(os.environ['PYTHONPATH'])
print_os_path(os.path)
# print(*os.environ['PYTHONPATH'].split(':'), sep='\n')
# if 'PYTHONPATH' in sorted(os.environ):
#     print(sys.path)
# else:
#     print('PYTHONPATH is not defined')"

# print(*a, sep = "\n")
