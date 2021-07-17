import requests
import json
import sys

rrid="Y2lzY29zcGFyazovL3VybjpURUFNOmV1LWNlbnRyYWwtMV9rL1JPT00vMWU0MzYyZDAtZGViZC0xMWViLTgxNGUtYjE1YWIxZjU0MzM2"
url1 = "https://webexapis.com/v1/messages"
accessToken="MTg4NWM3ZDgtMTgzMS00MTc0LTg3NzYtZmVhZTg2NmI3ZWMxOWJjZmQ3YTYtNGFj_PE93_bed4d195-92fc-4dd3-946a-c5b317a8386e"
url = 'https://webexapis.com/v1/rooms'
headers = {
    'Authorization': 'Bearer {}'.format(accessToken),
    'Content-Type': 'application/json'
}
params0={'max': '100'}
r = requests.get(url, headers=headers, params=params0)




#params={'max': '100'}


params1={
  "roomId": "Y2lzY29zcGFyazovL3VybjpURUFNOmV1LWNlbnRyYWwtMV9rL1JPT00vMWU0MzYyZDAtZGViZC0xMWViLTgxNGUtYjE1YWIxZjU0MzM2",
  "text": "nnnnn1"
}
rr=requests.post(url1,headers=headers,json=params1)

#re=requests.put(url,headers=headers,data=)
#response = requests.request("POST", url, headers=headers, data=payload, files=files)
#
gg=rr.json()
print(gg)
