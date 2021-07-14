import urllib.parse
import time
import requests
import json

Token=input("Input your access token: ")
if Token == "auto":
	accessToken = "Bearer your_code"
else: 
	accessToken=Token

apiUri="https://webexapis.com/v1/rooms"

r=requests.get(apiUri,
                headers={'Authorization':accessToken}
              )

json_data = r.json()

def name_all_group():
  noe=len(json_data["items"])
  name_group=[]
  n=0
  while True:
    if n<noe:
      x=json_data["items"][n]["title"]
      name_group.append(x) 
    else:
      break
    n=n+1
  return name_group
print("name of all group: ", name_all_group())