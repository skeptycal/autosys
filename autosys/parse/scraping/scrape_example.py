#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" This is an example of ways to extract data (numerical, photos, files, etc)
    from online resources. Using the existing tools can be frustrating and
    leads to an enourmous burden of recordkeeping and 'fiddling' with settings
    on CLI apps. A more complete way to solve the 90% problem that leaves out
    the 10% of edge cases where stuff is strange leads to a strikingly simpler
    way of doing thing.

    Some highlights are:

    ## Efficient Resource gathering:

    - Enter a url or search terms(for Google search)
    - choose resources to gather (photos, videos, html, text, css, etc)
    - gather entire contents or just links?
    - decide where to put the output (Dropbox, Docker, Google, AWS, local)
    - choose output format (files with html directory, csv, json, pdf, etc)
    - a way to choose priority, schedule a time to perform, etc
    - a way to share progress and data with coworkers
    - click 'go' and let it work ... no micromanaging / no boilerplate
    - notify on completion (text, email, log, etc)

    ## Parts needed to accomplish these goals:

    - A way to log in to Google for Search, Drive, Calendar, Notifications, etc
    - A way to log all activities with timestamps to provide a record and trace
    - A data structure to store the request information
    - A data structure to store the request results
    - A way to log in to Dropbox, AWS, Azure, etc to create files and folders
    - A way to set local and remote permissions on the data collection
    - A way to attach dataset to events in calendars and share with collaborators
    - A way to log and notify upon completion of various steps and milestones.


    # example of a background photo that was difficult to extract:
    # https://images.unsplash.com/photo-1463620695885-8a91d87c53d0?ixlib=rb-1.2.1
    # original url and tag: <iframe src="https://workona.com/newtab/chrome?type=wka&amp;bg=img&amp;galleries=3587225%2C3587267%2C3587269%2C3587264%2C3587279%2C3588045%2C3587324&amp;color=%232B86F1&amp;sb=hvr&amp;clock=true&amp;militaryTime=false&amp;v=442071" frameborder="0" style="position: fixed; top: 0px; right: 0px; bottom: 0px; left: 0px; height: 100vh; width: 100vw;"></iframe>
    """

from autosys import
