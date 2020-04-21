import logging

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
