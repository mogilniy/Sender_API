import os
import pickle
import sys
# Gmail API utils
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
# for encoding/decoding messages in base64
from base64 import urlsafe_b64decode, urlsafe_b64encode
# for dealing with attachement MIME types
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from mimetypes import guess_type as guess_mime_type
from google.oauth2.credentials import Credentials

our_email=sys.argv[1]
#accessToken="MTg4NWM3ZDgtMTgzMS00MTc0LTg3NzYtZmVhZTg2NmI3ZWMxOWJjZmQ3YTYtNGFj_PE93_bed4d195-92fc-4dd3-946a-c5b317a8386e"
name_room=sys.argv[2]
#name_room="DevNet_team_4"
send_mess=sys.argv[3]
to_email=sys.argv[4]
# Request all access (permission to read/send/receive emails, manage the inbox, and more)
SCOPES = ['https://mail.google.com/']
#our_email = 'g.mogilniy@gmail.com'
#SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']


##########################################
'''
def gmail_authenticate():
    creds = None
    # the file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first time
    if os.path.exists("token.pickle"):
        with open("token.pickle", "rb") as token:
            creds = pickle.load(token)
    # if there are no (valid) credentials availablle, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # save the credentials for the next run
        with open("token.pickle", "wb") as token:
            pickle.dump(creds, token)
    return build('gmail', 'v1', credentials=creds)

###################################
# Adds the attachment with the given filename to the given message
'''

def add_attachment(message, filename):
    content_type, encoding = guess_mime_type(filename)
    if content_type is None or encoding is not None:
        content_type = 'application/octet-stream'
    main_type, sub_type = content_type.split('/', 1)
    if main_type == 'text':
        fp = open(filename, 'rb')
        msg = MIMEText(fp.read().decode(), _subtype=sub_type)
        fp.close()
    elif main_type == 'image':
        fp = open(filename, 'rb')
        msg = MIMEImage(fp.read(), _subtype=sub_type)
        fp.close()
    elif main_type == 'audio':
        fp = open(filename, 'rb')
        msg = MIMEAudio(fp.read(), _subtype=sub_type)
        fp.close()
    else:
        fp = open(filename, 'rb')
        msg = MIMEBase(main_type, sub_type)
        msg.set_payload(fp.read())
        fp.close()
    filename = os.path.basename(filename)
    msg.add_header('Content-Disposition', 'attachment', filename=filename)
    message.attach(msg)


###################################

def build_message(destination, obj, body, attachments=[]):
    if not attachments: # no attachments given
        message = MIMEText(body)
        message['to'] = destination
        message['from'] = our_email
        message['subject'] = obj
    else:
        message = MIMEMultipart()
        message['to'] = destination
        message['from'] = our_email
        message['subject'] = obj
        message.attach(MIMEText(body))
        for filename in attachments:
            add_attachment(message, filename)
    return {'raw': urlsafe_b64encode(message.as_bytes()).decode()}

##############################

def send_message(service, destination, obj, body, attachments=[]):
    return service.users().messages().send(
      #userId="g.mogilniy@gmail.com",
      userId="me",
      body=build_message(destination, obj, body, attachments)
    ).execute()


# ##############################get the Gmail API service

def autent():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
          creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return creds       



#service = gmail_authenticate()
service = build('gmail', 'v1', credentials=autent())
'''
print ("=====================================")
print (service.users())
print ("=====================================")
print ("=====================================")
print ("=====================================")
'''
# test send email
send_message(service, "g.mogilniy@gmail.com", "Copy mess"+name_room, 
            send_mess+to_email,[] )
#send_message(service, "mischuk.ieo@knuba.edu.ua", "This is a subject from python", 
#            "This is the body of the email ????? ", [])            