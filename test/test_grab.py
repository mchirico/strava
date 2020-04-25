from unittest import TestCase
from pprint import pprint
from grab.grab import Grab
from collect_athlete_data.collect import Activity, BigQInsert, StorageInsert
from storage.storage import Buckets
from token_utils.token import get_test_access


class GrabTestSuite(TestCase):

    def test_activity(self):
        before = 1587426805
        after = 1577922712
        access_token = get_test_access()

        grab = Grab(access_token, before, after)
        grab.bq_insert().storage_collect()
