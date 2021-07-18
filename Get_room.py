import urllib.parse
import time
import requests
import json
import sys

apiUri="https://webexapis.com/v1/rooms"

#accessToken=""
accessToken=sys.argv[1]
#print(accessToken)
#access_token = 'your_token_here'  
url = 'https://webexapis.com/v1/rooms'
headers = {
    'Authorization': 'Bearer {}'.format(accessToken),
    'Content-Type': 'application/json'
}
params={'max': '100'}
r = requests.get(url, headers=headers, params=params)





'''
r=requests.get(apiUri,
                headers={'Token':accessToken}
              )
'''
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
temp=name_all_group()
intl=len(temp)
i=0
ii=0
while ii<intl:
      print(temp[ii])
      ii=ii+1
