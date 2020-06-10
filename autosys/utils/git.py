#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# from https://github.com/c4urself/bump2version

import errno
import logging
import os
import subprocess
from tempfile import NamedTemporaryFile

from autosys.exceptions import (
    MercurialDoesNotSupportSignedTagsException,
    WorkingDirectoryIsDirtyException,)
from autosys.lister import *

logger = logging.getLogger(__name__)


class BaseVCS:

    _TEST_USABLE_COMMAND = None
    _COMMIT_COMMAND = None

    @classmethod
    def commit(cls, message, context, extra_args=None):
        extra_args = extra_args or []
        with NamedTemporaryFile("wb", delete=False) as f:
            f.write(message.encode("utf-8"))
        env = os.environ.copy()
        env["HGENCODING"] = "utf-8"
        for key in ("current_version", "new_version"):
            env[str("BUMPVERSION_" + key.upper())] = str(context[key])
        try:
            subprocess.check_output(
                cls._COMMIT_COMMAND + [f.name] + extra_args, env=env
            )
        except subprocess.CalledProcessError as exc:
            err_msg = "Failed to run {}: return code {}, output: {}".format(
                exc.cmd, exc.returncode, exc.output
            )
            logger.exception(err_msg)
            raise exc
        finally:
            os.unlink(f.name)

    @classmethod
    def is_usable(cls):
        try:
            return (
                subprocess.call(
                    cls._TEST_USABLE_COMMAND,
                    stderr=subprocess.PIPE,
                    stdout=subprocess.PIPE,
                )
                == 0
            )
        except OSError as e:
            if e.errno in (errno.ENOENT, errno.EACCES):
                return False
            raise


class Git(BaseVCS):

    _TEST_USABLE_COMMAND = ["git", "rev-parse", "--git-dir"]
    _COMMIT_COMMAND = ["git", "commit", "-F"]
    _GIT_ADD_ALL = ["git", "add", "-all"]
    _GIT_COMMIT_AUTO = [
        "git",
        "commit",
        "-m",
        "The Great Gitspy autoformatting / refactoring.",
    ]
    _GIT_PUSH = ["git", "push", "--signed"]
    _GIT_PUSH_SUP = "git push --set-upstream origin $(git_current_branch)"

    @classmethod
    def assert_nondirty(cls):
        lines = [
            line.strip()
            for line in subprocess.check_output(
                ["git", "status", "--porcelain"]
            ).splitlines()
            if not line.strip().startswith(b"??")
        ]

        if lines:
            raise WorkingDirectoryIsDirtyException(
                "Git working directory is not clean:\n{}".format(
                    b"\n".join(lines).decode()
                )
            )

    @classmethod
    def latest_tag_info(cls):
        try:
            # git-describe doesn't update the git-index, so we do that
            subprocess.check_output(["git", "update-index", "--refresh"])

            # get info about the latest tag in git
            describe_out = (
                subprocess.check_output(
                    [
                        "git",
                        "describe",
                        "--dirty",
                        "--tags",
                        "--long",
                        "--abbrev=40",
                        "--match=v*",
                    ],
                    stderr=subprocess.STDOUT,
                )
                .decode()
                .split("-")
            )
        except subprocess.CalledProcessError:
            logger.debug("Error when running git describe")
            return {}

        info = {}

        if describe_out[-1].strip() == "dirty":
            info["dirty"] = True
            describe_out.pop()

        info["commit_sha"] = describe_out.pop().lstrip("g")
        info["distance_to_latest_tag"] = int(describe_out.pop())
        info["current_version"] = "-".join(describe_out).lstrip("v")

        return info

    @classmethod
    def add_path(cls, path):
        subprocess.check_output(["git", "add", "--update", path])

    @classmethod
    def tag(cls, sign, name, message):
        command = ["git", "tag", name]
        if sign:
            command += ["-s"]
        if message:
            command += ["--message", message]
        subprocess.check_output(command)


hr(n=60)
print(dir())
