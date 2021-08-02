import urllib.parse
import time
import requests
import json
import sys

apiUri="https://webexapis.com/v1/rooms"

#accessToken="Zjg2YTBlMGUtMWFhOC00ODYwLWI0MjgtOTc1MTNjNDAzODMxYTY5YTEzMzAtMDEz_PE93_bed4d195-92fc-4dd3-946a-c5b317a8386e"
accessToken=sys.argv[1]
#print(accessToken)

 
url = 'https://webexapis.com/v1/rooms'
headers = {
    'Authorization': 'Bearer {}'.format(accessToken),
    'Content-Type': 'application/json'
}
params={'max': '100'}
r = requests.get(url, headers=headers, params=params)

json_data = r.json()

def name_all_group():
  noe=len(json_data["items"])
  name_group=[]
  n=0
  while n<noe:
      x=json_data["items"][n]["title"]
      name_group.append(x)   
      n=n+1
  return name_group
temp=name_all_group()
intl=len(temp)

ii=0
while ii<intl:
      print(temp[ii])
      ii=ii+1
