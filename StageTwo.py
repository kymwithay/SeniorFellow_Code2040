#Kymberlee Hill
#Code2040 - Stage Two
#Needle In A Haystack

import json
import requests
import ast
from datetime import timedelta

token = raw_input("Please enter your token: ")
code2040 = "http://challenge.code2040.org/api/"


request = requests.post(code2040 + "haystack", json = {"token": token})

if request.status_code == 200:
    responseDict = ast.literal_eval(request.content)
    needle = responseDict['needle']
    haystack = responseDict['haystack']
    
    foundNeedle = False # keeps track of whether the needle was found or not

    for i in range(0, len(haystack)):
        if needle == haystack[i]:
            request = requests.post(code2040 + "haystack/validate",
                json = {"token": token, "needle": str(i)})
            foundNeedle = True
            break

    if foundNeedle and request.status_code == 200:
        print "Finished part 3"
    elif foundNeedle == False:
        print "Finished part 3 - couldn't find the needle in the haystack"
    else:
        print "FAILED PART 3: error in second request"
else:
    print "FAILED PART 3: error in first request"