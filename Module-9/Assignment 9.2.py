# Mirach Erkol
# 11/30/2025
# CSD325-340A
# Assignment 9.2

'''Create a program that includes the following:
    Find a simple API. The link above has a couple that you can work with, but the examples are not in Python...the concept is the same..
    Test the connection to your API, output results.
    Print out the response from the request, with no formatting.
    Print out the response with same formatting as the tutorial program.
    Run the program and take a screenshot of the results. Paste that screenshot into your Word document.'''

import requests
import json

'''Program that uses the market API for one of my favorite online games to look up item data.'''

# This example looks up the Abyssal whip (item id 4151)
url = "https://services.runescape.com/m=itemdb_oldschool/api/catalogue/detail.json"
params = {"item": 4151}

# Test the connection to the API
response = requests.get(url, params=params)

# 1) Output the status code to show the connection worked
print("status code:", response.status_code)

# 2) Print out the response with no formatting
print("\nRaw response (unformatted):")
print(response.text)

# 3) Same response, but formatted like the tutorial program
def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

print("\nFormatted JSON response:")
jprint(response.json())