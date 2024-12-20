import os
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from errlog import log


SERVICE_ACCOUNT_FILE = 'serviceaccount.json'

if not os.path.exists(SERVICE_ACCOUNT_FILE):
    SERVICE_ACCOUNT_FILE = input("enter the filename of your service account: ")
    if not SERVICE_ACCOUNT_FILE.endswith(".json"):
        SERVICE_ACCOUNT_FILE = f"{SERVICE_ACCOUNT_FILE}.json"

SCOPES = ['https://www.googleapis.com/auth/documents']

creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
service = build('docs', 'v1', credentials=creds)


def googledoc(doc_id):

    try:
        doc = service.documents().get(documentId=doc_id).execute()
        content = []
        for element in doc.get('body', {}).get('content', []):
            if 'paragraph' in element:
                for run in element['paragraph'].get('elements', []):
                    if 'textRun' in run:
                        content.append(run['textRun']['content'])
        return ''.join(content)

    except Exception as e:
        return e


def editdoc(doc_id, requests):
    response = service.documents().batchUpdate(
        documentId=doc_id,
        body={'requests': requests}
    ).execute()
    print(response)
