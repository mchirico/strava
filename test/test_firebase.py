from unittest import TestCase
from firebase.firebase import db, UserData
from credentials.creds import Auth
import json


class FirebaseTestSuite(TestCase):
    """Firebase cases."""

    def test_firebase(self):
        doc_ref = db.collection(u'strava').document(u'runner').collection(
            u'name').document('stuff')
        doc_ref.set({
            u'first': u'Mike',
            u'last': u'Chirico',
            u'born': 1815
        })

    def test_read(self):
        users_ref = db.collection(u'strava').document(u'runner').collection(
            u'name')
        docs = users_ref.stream()

        for doc in docs:
            print(u'{} => {}'.format(doc.id, doc.to_dict()))

    def test_UserData(self):
        u = UserData('0', 'smith', 'john', '99b', '99b', 1587499052)
        u.update()

    def test_SampleData(self):
        a = Auth(3)
        s = a.sampleData()
        j = json.loads(s)
        print(j)

