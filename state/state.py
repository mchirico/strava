from firebase.firebase import db

import datetime


class State:

    def __init__(self, state):
        self._state = str(state)

    def insert(self):
        now = datetime.datetime.now()
        timeStamp = now.strftime("%Y-%m-%dT%H:%M:%S.%s")
        timeStamp_epoch = now.timestamp()
        doc_ref = db.collection(u'strava').document(
            str('state')).collection(
            str(self._state)).document('version 0')
        doc_ref.set({
            u'state': self._state,
            u'status': 'initial',
            u'timeStamp': timeStamp,
            u'timeStamp_epoch': timeStamp_epoch
        })

    def delete(self):
        db.collection(u'strava').document(u'state').collection(
            str(self._state)).document('version 0').delete()

    def read(self):
        doc_ref = db.collection(u'strava').document(u'state').collection(
            str(self._state))
        docs = doc_ref.stream()

        self._records = []
        for doc in docs:
            self.records.append(doc.to_dict())
            print(u'{} => {}'.format(doc.id, doc.to_dict()))


    @property
    def state(self):
        return self._state
