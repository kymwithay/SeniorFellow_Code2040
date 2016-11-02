#Kymberlee Hill
#Registration - Part one

import json
import requests
import ast
from datetime import timedelta

token = raw_input("Please enter your token: ")
code2040 = "http://challenge.code2040.org/api/"

#  ------  PART 1  ------  #

request = requests.post(code2040 + "register",
    json = {"token": token,
    "github": "https://github.com/kymwithay/SeniorFellow_Code2040"})

if request.status_code == 200:
    print "Finished part 1"
else:
    print "FAILED PART 1: error in request"


