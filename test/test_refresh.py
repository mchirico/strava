from unittest import TestCase
from firebase.firebase import db

from token_utils.token import RefreshDatabaseUpdate, get_test_access


class RefreshTestSuite(TestCase):

    def test_refresh(self):
        lastname = 'test'
        id = 55529309
        refresh = RefreshDatabaseUpdate(db, lastname, id)

        print(refresh.seconds_left)
        refresh.doRefresh()
        print(refresh.access_token)

    def test_get_test_access(self):
        print(get_test_access())