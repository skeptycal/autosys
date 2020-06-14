#!/usr/bin/env python3
# 'Standard Library'
import sys

# 'third party'
from isort.hooks import git_hook

sys.exit(git_hook(strict=True, modify=True))
