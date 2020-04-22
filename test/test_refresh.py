from unittest import TestCase
from firebase.firebase import db, UserData
from credentials.creds import Auth
from token_utils.token import RefreshDatabaseUpdate
import json
import time


class RefreshTestSuite(TestCase):

    def test_refresh(self):

        lastname = 'test'
        id = 55529309
        refresh = RefreshDatabaseUpdate(db,lastname,id)

        print(refresh.seconds_left)
        refresh.doRefresh()