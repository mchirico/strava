from unittest import TestCase
from firebase.firebase import db


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
