import logging
import time

from credentials.creds import RefreshToken
from firebase.firebase import UserData


class Token:

    def __init__(self, request):
        self.request = request
        self._status = False
        self.extract()

    def extract(self):
        try:
            self._state = self.request.args.get('state')
            self._code = self.request.args.get('code')
            self._scope = self.request.args.get('scope')
        except KeyError:
            self._status = False
        self._status = True

    @property
    def status(self):
        return self._status

    @property
    def state(self):
        return self._state

    @property
    def scope(self):
        return self._scope

    @property
    def code(self):
        return self._code


class HandleCreds:

    def __init__(self, token, credentials,
                 UserData, session):
        if token.status:
            a = credentials.creds.Auth(token.code)
            d = a.getAuth()
            logging.warning("d: {}".format(d))
            if 'expires_at' in d:
                u = UserData(d['athlete']['id'], d['athlete']['lastname'],
                             d['athlete']['firstname'],
                             d['access_token'],
                             d['refresh_token'], d['expires_at'])
                u.update()
                session['id'] = d['athlete']['id']
                session['lastname'] = d['athlete']['lastname']
                session['firstname'] = d['athlete']['firstname']
                session['expires_at'] = d['expires_at']
                session['access_token'] = d['access_token']


class RefreshDatabaseUpdate:

    def __init__(self, db, lastname, id):
        users_ref = db.collection(u'strava').document(lastname).collection(
            str(id))
        docs = users_ref.stream()

        for doc in docs:
            result = doc.to_dict()
            print(u'{} => {}'.format(doc.id, doc.to_dict()))
        self._result = result

    @property
    def seconds_left(self):
        return self._result.get("expires_at", 0) - int(time.time())

    @property
    def result(self):
        return self._result

    @property
    def refresh_result(self):
        return self._rresult

    def doRefresh(self):
        if self.seconds_left < 1:
            return
        refresh_token = self._result.get("refresh_token", False)
        if refresh_token:
            rt = RefreshToken(refresh_token)
            self._rresult = rt.refresh()
            self.updateDb()

    def updateDb(self):
        id = self._result['id']
        lastname = self._result['lastname']
        firstname = self._result['firstname']
        access_token = self._rresult['access_token']
        refresh_token = self._rresult['refresh_token']
        expires_at = self._rresult['expires_at']
        u = UserData(id, lastname,
                     firstname,
                     access_token,
                     refresh_token, expires_at)
        u.update()





