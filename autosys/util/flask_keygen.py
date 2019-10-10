#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" flask_keygen.py """
# copyright (c) 2019 Michael Treanor
# https://www.github.com/skeptycal

import secrets

flask_key: bytes = secrets.token_bytes(24)

if __name__ == "__main__":
    key_str: str = str(flask_key)
    print("")
    print("*" * 79)
    print("New, unique FLASK_SECRET_KEY generated: ")
    print("")
    print(" bytes: ", flask_key)
    print("string: ", key_str)
    print("")

# References:
#   modifications to dev cycle and file structure inspired by:
#       https://github.com/aeroxis/sultan
#   Reference for FLASK_SECRET_KEY:
#       https://stackoverflow.com/questions/22463939/demystify-flask-app-secret-key
