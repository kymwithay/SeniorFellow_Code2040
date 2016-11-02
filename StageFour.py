#Kymberlee Hill
#Code2040 - Stage Four
#Dating
import json
import dateutil.parser
import requests
import ast
from datetime import timedelta


token = raw_input("Please enter your token: ")
code2040 = "http://challenge.code2040.org/api/"

request = requests.post(code2040 + "dating", json = {"token": token})

if request.status_code == 200:
    responseDict = ast.literal_eval(request.content)
    receivedDate = dateutil.parser.parse(responseDict["datestamp"])
    newDate = receivedDate + timedelta(seconds = responseDict["interval"])
    newDateString = newDate.isoformat()[:-6] + "Z"
    request = requests.post(code2040 + "/dating/validate",
        json = {"token": token, "datestamp": newDateString})
    if request.status_code == 200:
        print "Finished part 5"
    else:
        print "FAILED PART 5: error in second request"
else:
    print "FAILED PART 5: error in first request"
