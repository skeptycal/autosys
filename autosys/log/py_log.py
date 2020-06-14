""" # * From pywall - see description at the end of this file

Contains code to setup logging, and to run the logger process.

Sadly, logging in multiprocessing programs is not trivial.  Happily, Python
provides wonderful logging utilities that make multiprocessing logging much
nicer to setup.  We use these utilities here.  The external "logutils" module
actually contains logging library items that are present in Python 3,
backported to Python 2.

"""

# 'Standard Library'
import logging
import time

from logging import (
    FileHandler,
    StreamHandler,
)

# 'package imports'
from logutils.queue import (
    QueueHandler,
    QueueListener,
)


def _get_formatter():
    """Creates a formatter with our specified format for log messages."""
    return logging.Formatter(fmt="[%(asctime)s][%(levelname)s] %(message)s")


def initialize_logging(level, queue):
    """Setup logging for a process.

    Creates a base logger for pywall.  Installs a single handler, which will
    send packets across a queue to the logger process.  This function should be
    called by each of the three worker processes before they start.

    """
    formatter = _get_formatter()

    logger = logging.getLogger("pywall")
    logger.setLevel(level)

    handler = QueueHandler(queue)
    handler.setLevel(level)
    handler.setFormatter(formatter)

    logger.addHandler(handler)


def log_server(level, queue, filename, mode="w"):
    """Run the logging server.

    This listens to the queue of log messages, and handles them using Python's
    logging handlers.  It prints to stderr, as well as to a specified file, if
    it is given.

    """
    formatter = _get_formatter()
    handlers = []

    sh = StreamHandler()
    sh.setFormatter(formatter)
    sh.setLevel(level)
    handlers.append(sh)

    if filename:
        fh = FileHandler(filename, mode)
        fh.setFormatter(formatter)
        fh.setLevel(level)
        handlers.append(fh)

    listener = QueueListener(queue, *handlers)
    listener.start()

    # For some reason, queuelisteners run on a separate thread, so now we just
    # "busy wait" until terminated.
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        pass
    finally:
        listener.stop()


""" #*#####################################################################

PyWall
======

A Python firewall: Because slow networks are secure networks.


Installation
------------

This section assumes that you are installing this program on Ubuntu 14.04 LTS.
This firewall should work on other Linux systems, but safety not guaranteed.

First, install the required packages. On Ubuntu, these are `iptables`, `python`,
`python-pip`, `build-essential`, `python-dev`, and
`libnetfilter-queue-dev`. Next, use `pip2` to install the project dependencies,
which can be found in `requirements.txt`.

The commands for both these operations are:

    sudo apt-get install python python-pip iptables build-essential python-dev libnetfilter-queue-dev
    pip install --user -r requirements.txt


Running
-------

The main file is `main.py`, which needs to be run as root to modify IPTables.
Additionally, main needs to receive a JSON configuration file as its first
argument. If running with the example configuration, the command is:

`sudo python2 main.py examples/example.json`

To stop PyWall, press Control-C.


Troubleshooting
---------------

PyWall should undo its changes to IPTables after exiting. However, if you are
unable to access the internet after exiting PyWall, view existing
IPTables rules with `sudo iptables -nL`. If a rule with the target chain
`NFQueue` lingers, delete it with
`sudo iptables -D INPUT -j NFQUEUE --queue-num [undesired-queue-number]`.

For INPUT rules, the command is `sudo iptables -D INPUT -j NFQUEUE --queue-num 1`.
For OUTPUT rules, the command is `sudo iptables -D OUTPUT -j NFQUEUE --queue-num 2`.

In case PyWall gives a message that another application has the xtables lock,
Control-C the server, ensure that all the IPTables rules are cleared, and
restart PyWall.

"""
