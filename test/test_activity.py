from unittest import TestCase
from firebase.firebase import db
from pprint import pprint
from token_utils.token import RefreshDatabaseUpdate, get_test_access
from collect_athlete_data.collect import Activity, BigQInsert
from token_utils.token import get_test_access



class ActivityTestSuite(TestCase):

    def test_activity(self):
        before = 1587426805
        after = 1577922712
        activity = Activity(get_test_access())
        r = activity.get_activity(before,after)
        pprint(r)


    def test_bqinsert(self):
        before = 1587426805
        after = 1577922712
        activity = Activity(get_test_access())
        r = activity.get_activity(before,after)
        bqi = BigQInsert()
        bqi.insertraw(before, after, r)
