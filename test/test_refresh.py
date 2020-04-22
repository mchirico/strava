from unittest import TestCase
from firebase.firebase import db

from token_utils.token import RefreshDatabaseUpdate


class RefreshTestSuite(TestCase):

    def test_refresh(self):
        lastname = 'test'
        id = 55529309
        refresh = RefreshDatabaseUpdate(db, lastname, id)

        print(refresh.seconds_left)
        refresh.doRefresh()
        print(refresh.access_token)
