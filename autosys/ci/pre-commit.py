#!/usr/bin/env python3
import sys
from isort.hooks import git_hook

sys.exit(git_hook(strict=True, modify=True))
