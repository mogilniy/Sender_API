import urllib.parse
import time
import requests
import json

accessToken=input("Input your access token: ")

name_room=input("Input name of your room: ")

apiUri="https://webexapis.com/v1/rooms"

r=requests.get(apiUri,
                headers={'Authorization':accessToken}
              )

json_data = r.json()

def id_room():
    count=0
    for i in json_data["items"]:
        count=count+1
        if json_data["items"][count]["title"]==name_room:
            #print("Room name : " + json_data["items"][count]["title"]+"\n"+"Room id: " +json_data["items"][count]["id"])
            y=json_data["items"][count]["id"]
            break
        else:
            continue
    return y


uri_member="https://webexapis.com/v1/memberships?"
roomId=id_room()

t=requests.get(uri_member+"roomId="+roomId,
                headers={'Authorization':accessToken}
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

print (id_room())
print(list_of_email())

