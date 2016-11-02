#Kymberlee Hill
#Code2040 - Stage One
#ReversedString
import json
import requests
import ast
from datetime import timedelta

token = raw_input("Please enter your token: ")
code2040 = "http://challenge.code2040.org/api/"

request = requests.post(code2040 + "reverse", json = {"token": token})

if request.status_code == 200:
    reversedString = str(request.content)[::-1]
    request = requests.post(code2040 + "reverse/validate",
        json = {"token": token, "string": reversedString})
    if request.status_code == 200:
        print "Finished part 2"
    else:
        print "FAILED PART 2: error in second request"
else:
    print "FAILED PART 2: error in first request"

