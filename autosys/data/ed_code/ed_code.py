#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# 'Standard Library'
import os

from functools import lru_cache
from pathlib import Path

from typing import List

# root search path
search_path: str = Path().cwd().as_posix()


# !-------------------- Target Extensions list
# We only are interested in these file types
targets = ["html", "txt"]

# !-------------------- Exclusions list
# If the file path contains these we dont want them
#    eg. C:\\Directory\\ForWalking\\node_modules will be ignored
exclusions = ["node_modules", "SolutionFiles", ".bin", "Test"]


# @lru_cache
def get_list(
    search_path: str = search_path,
    targets: List[str] = targets,
    exclusions: List[str] = exclusions,
    recursive: bool = True,
):
    """ #### Return a list of files

        - <search_path> - root path for recursive search
        - <targets> - list of globs to locate
        - <exclusions> - list of globs to exclude
        - <recursive> -
        """

    # Array to store all our file paths
    file_paths = []

    for root, sub_dirs, file_names in os.walk(search_path):

        # Check each file against the <targets>
        #   and <exclusions> lists
        for file_name in file_names:

            # If the file path includes files with extensions
            #   from the targets list ...
            if any(target in root for target in targets):

                # ... and if the file path doesnt have the exclusion list,
                #   add it to the file_paths list
                if not any(exclusion in root for exclusion in exclusions):
                    file_paths.append(os.path.join(root, file_name))


file_paths: List[str] = get_list()
print(file_paths)
