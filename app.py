import os
import threading
import atexit
import time
import credentials
from grab.grab import Grab

from flask import Flask, request, session
from firebase.firebase import db, UserData
from token_utils.token import Token, HandleCreds, ClearSession
import logging

POOL_TIME = 3000  # Seconds

# variables that are accessible from anywhere
commonDataStruct = 0
# lock to control access to variable
dataLock = threading.RLock()
# thread handler
yourThread = threading.Thread()


def create_app():
    app = Flask(__name__)
    app.secret_key = credentials.creds.secretSessionKey()

    @app.route('/logout', methods=['POST', 'GET'])
    def logout():
        ClearSession(session)
        return 'done'

    @app.route('/test', methods=['GET', 'POST'])
    def my_test():
        return 'test'

    @app.route('/grabdata', methods=['POST', 'GET'])
    def grab_data():
        access_token = session.get('access_token', False)
        if access_token:
            before = 1587426805
            after = 1577922712
            grab = Grab(access_token, before, after)
            grab.storage_collect()
            return 'success'
        return 'grab'

    @app.route('/auth', methods=['POST', 'GET'])
    def auth():
        if request.method == 'POST':
            return 'post: {}\n'.format(request)
        else:
            token = Token(request)
            logging.warning('token.code'.format(token.code))
            HandleCreds(token, credentials, UserData, session)
            access_token = session.get('access_token', False)
            if access_token:
                return access_token
            return 'Something went wrong'

        return 'Could not get code:'

    @app.route('/')
    def hello_world():
        state = "aabk3amikelasplst"
        link = "https://www.strava.com/oauth/authorize?client_id=7704&state" \
               "={}" \
               "&redirect_uri=https://" \
               "strava.montcopa.io/auth&response_type" \
               "=code&scope=read_all,activity:read_all," \
               "profile:read_all".format(state)

        id = session.get('id', '')
        lastname = session.get('lastname', '')
        firstname = session.get('firstname', '')
        expires_at = session.get('expires_at', 0)
        if expires_at < int(time.time()):
            return '\ncount: {}\n' \
                   '<a href="{}">auth</a>' \
                   ''.format(commonDataStruct, link)
        else:
            return 'Hi {} {} {}'.format(firstname, lastname, id)

    def interrupt():
        global yourThread
        yourThread.cancel()

    def doStuff():
        global commonDataStruct
        global yourThread
        with dataLock:
            commonDataStruct += 1
        #            p = PubSub()
        #            p.send()
        #            p.readMsgProcess(POOL_TIME-2)
        # Set the next thread to happen
        yourThread = threading.Timer(POOL_TIME, doStuff, ())
        yourThread.start()

    def doStuffStart():
        # Do initialisation stuff here
        global yourThread
        # Create your thread
        yourThread = threading.Timer(POOL_TIME, doStuff, ())
        yourThread.start()

    # Initiate
    # For now turning this off
    # doStuffStart()
    # When you kill Flask (SIGTERM), clear the trigger for the next thread
    atexit.register(interrupt)
    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
