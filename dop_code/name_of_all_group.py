import urllib.parse
import time
import requests
import json

Token=input("Input your access token: ")
if Token == "auto":
	accessToken = "Bearer ZDNhZDIyN2ItNjhmNi00MjE3LTgzNjQtNDA4OTVlZDNkOWNhMGFmYjcxMzYtZTJk_P0A1_958dad28-3e63-44bf-8f25-05fbd7ae4937"
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
def get_rooms():
  s=""
  for i in name_all_group():
    s=s+i+"\n"
  return s

#print(get_rooms())

    