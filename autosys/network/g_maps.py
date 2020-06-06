#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# Reference:
# https://www.geeksforgeeks.org/python-get-google-map-image-specified-location-using-google-static-maps-api/

# Google API Key and account:
# https://developers.google.com/maps/documentation/maps-static/intro

# Python program to get a google map
# image of specified location using
# Google Static Maps API

# importing required modules
import requests

# Enter your api key here
api_key = "_your_api_key_"

# url variable store url
url = "https://maps.googleapis.com/maps/api/staticmap?"

# center defines the center of the map,
# equidistant from all edges of the map.
center = "Dehradun"

# zoom defines the zoom
# level of the map
zoom = 10

# get method of requests module
# return response object
r = requests.get(
    url
    + "center ="
    + center
    + "&zoom ="
    + str(zoom)
    + "&size = 400x400&key ="
    + api_key
    + "sensor = false"
)

# wb mode is stand for write binary mode
f = open("address of the file location ", "wb")

# r.content gives content,
# in this case gives image
f.write(r.content)

# close method of file object
# save and close the file
f.close()
