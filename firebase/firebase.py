import firebase_admin
from firebase_admin import credentials, firestore
import os.path

from utils.util import findFile
import time
import datetime

os.environ['TZ'] = 'US/Eastern'
time.tzset()

cred = credentials.Certificate(findFile("firebase.json"))
firebase_admin.initialize_app(cred)
db = firestore.client()


class UserData:

    def __init__(self, id, lastname, firstname, access_token,
                 refresh_token, expires_at):
        self.id = id
        self.lastname = lastname
        self.firstname = firstname
        self.access_token = access_token
        self.refresh_token = refresh_token
        self.expires_at = expires_at

    def update(self):
        now = datetime.datetime.now()
        timeStamp = now.strftime("%Y-%m-%dT%H:%M:%S.%s")
        timeStamp_epoch = now.timestamp()
        doc_ref = db.collection(u'strava').document(
            str(self.lastname)).collection(
            str(self.id)).document(str(self.firstname))
        doc_ref.set({
            u'id': self.id,
            u'lastname': self.lastname,
            u'firstname': self.firstname,
            u'access_token': self.access_token,
            u'refresh_token': self.refresh_token,
            u'expires_at': self.expires_at,
            u'timeStamp': timeStamp,
            u'timeStamp_epoch': timeStamp_epoch
        })


