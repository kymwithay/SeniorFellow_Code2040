#Kymberlee Hill
#Code2040 - Stage Three
#Prefix
import json
import requests
import ast
from datetime import timedelta


token = raw_input("Please enter your token: ")
code2040 = "http://challenge.code2040.org/api/"

request = requests.post(code2040 + "prefix", json = {"token": token})

if request.status_code == 200:
    responseDict = ast.literal_eval(request.content)
    prefix = responseDict['prefix']
    receivedArray = responseDict['array']
    responseArray = []
    for i in range(0, len(receivedArray)):
        if not receivedArray[i].startswith(prefix):
            responseArray.append(receivedArray[i])
    
    request = requests.post(code2040 + "prefix/validate",
        json = {"token": token, "array": responseArray})
    
    if request.status_code == 200:
        print "Finished part 4"
    else:
        print "FAILED PART 4: error in second request"
else:
    print "FAILED PART 4: error in first request"