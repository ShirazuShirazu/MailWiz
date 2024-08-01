# Service/emailservice.py

from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime
from Models.email import Email
from authenticateEmail import createGmailService
from main import getSession

requiredValues = ["From", "Subject", "Date"]


def fetchEmails(session):
    service = createGmailService()
    
    # Call the Gmail API
    results = service.users().messages().list(userId='me').execute()
    messages = results.get('messages', [])

    if not messages:
        print('No messages found.')
    else:
        print('Messages:')
        for message in messages:
            msg = service.users().messages().get(userId='me',
                                                  id=message['id'],
                                                  format = "metadata",
                                                  metadataHeaders=requiredValues
                                                  ).execute()
            # print(f"Message snippet: {msg}")
            saveEmail(session, msg)

    return messages

def saveEmail(session, msg):

    header_to_attr = {
    "From": "from_address",
    "Subject": "subject",
    "Date": "date_received"
    }

    email = Email(
        email_id=msg['id'],
        message=msg['snippet'] 
    )
    for header in msg['payload']['headers']:
        if header['name'] in requiredValues:
            value = header['value']
            if header['name'] == "Date":
                value = datetime.datetime.strptime(value, '%a, %d %b %Y %H:%M:%S %z')
                value = value.replace(tzinfo=None) 
            setattr(email, header_to_attr[header['name']], value)
    
    print(email)

    session.add(email)
    session.commit()
    


if __name__ == '__main__':
    session = getSession()
    fetchEmails(session)

