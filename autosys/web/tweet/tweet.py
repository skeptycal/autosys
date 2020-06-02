#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import tweepy

# AUTHenticate to Twitter
AUTH = tweepy.OAUTHHandler("CONSUMER_KEY", "CONSUMER_SECRET")
AUTH.set_access_token("ACCESS_TOKEN", "ACCESS_TOKEN_SECRET")

# Create API object
api = tweepy.API(AUTH)

# Create a tweet
api.update_status("Hello Tweepy")
