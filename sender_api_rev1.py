import urllib
import time
import requests
import json

choice = input("Do you want to use the hard-coded token? (y/n)")

if choice == "N" or choice == "n":
	accessToken = input("Enter your access token: ")
	accessToken = "Bearer " + accessToken
else: 
	accessToken = "Bearer ..................."

print(accessToken)

apiUri="https://webexapis.com/v1/rooms"

r=requests.get(apiUri,
                headers={'Authorization':accessToken}
              )

if(r.status_code != 200):
    print("Something wrong has happened:")
    print("ERROR CODE: {} \nRESPONSE: {}".format(r.status_code, r.text))
    assert()

json_data = r.json()

print("Webex Teams Response Data:") 
print( json.dumps(json_data, indent = 4) )


