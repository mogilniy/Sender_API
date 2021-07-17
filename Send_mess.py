import urllib.parse
import time
import requests
import json
import sys

from requests.api import request


apiUri="https://webexapis.com/v1/rooms"

#accessToken=sys.argv[1]
accessToken="MTg4NWM3ZDgtMTgzMS00MTc0LTg3NzYtZmVhZTg2NmI3ZWMxOWJjZmQ3YTYtNGFj_PE93_bed4d195-92fc-4dd3-946a-c5b317a8386e"
#name_room=sys.argv[2]
name_room="DevNet_team_4"
#send_mess=sys.argv[3]
send_mess="sen 1 mes"
#print(accessToken)
#access_token = 'your_token_here'  
url = 'https://webexapis.com/v1/rooms'
headers = {
    'Authorization': 'Bearer {}'.format(accessToken),
    'Content-Type': 'application/json'
}
params={'max': '100'}

r = requests.get(url, headers=headers, params=params)




json_data = r.json()

def id_room():
    count=0
    for i in json_data["items"]:
        #print (json_data["items"][count]["title"])
        
        if json_data["items"][count]["title"]==name_room:
            #print("Room name : " + json_data["items"][count]["title"]+"\n"+"Room id: " +json_data["items"][count]["id"])
            y=json_data["items"][count]["id"]
            break
        else:
            count=count+1
            continue
    return y


uri_member="https://webexapis.com/v1/memberships?"
roomId=id_room()

t=requests.get(uri_member+"roomId="+roomId,
               headers=headers, params=params
              )

json_data_t = t.json()

def list_of_email():
    k=0
    list_e=""
    for e in json_data_t["items"]:
        k=k+1
        list_e=list_e+e["personEmail"]+"\n"
        #print ("Email {}: ".format(k)+e["personEmail"])
    return list_e

#print (id_room())

print(list_of_email())
params={'roomId': roomId, "text": send_mess}
uri_member="https://webexapis.com/v1/messages"
t=requests.put(uri_member,
               headers=headers, params=params
              )
t1=requests.put(uri_member,headers=headers,params=params)
json_data_t = t.json()
print (json_data_t)              

