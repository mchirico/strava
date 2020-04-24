from unittest import TestCase
from firebase.firebase import db
from pprint import pprint
from token_utils.token import RefreshDatabaseUpdate, get_test_access
from collect_athlete_data.collect import Activity, BigQInsert, StorageInsert
from storage.storage import Buckets
from token_utils.token import get_test_access


class ActivityTestSuite(TestCase):

    def test_activity(self):
        before = 1587426805
        after = 1577922712
        activity = Activity(get_test_access())
        r = activity.get_activity(before, after)
        pprint(r)

    def test_bqinsert(self):
        before = 1587426805
        after = 1577922712
        activity = Activity(get_test_access())
        r = activity.get_activity(before, after)
        bqi = BigQInsert()
        bqi.insertraw(before, after, r)

    def test_storage_insert(self):
        before = 1587730062
        after = 1577922712
        activity = Activity(get_test_access())
        r = activity.get_activity(before, after)
        athlete_id = r[0].athlete.id
        b = Buckets()

        file = 'summary/%s/%s/%s/raw.json' % (athlete_id, before, after)
        b.createFromString(file, str(r).encode())

    def test_storage_individual(self):
        before = 1587730062
        after = 1577922712
        activity = Activity(get_test_access())
        r = activity.get_activity(before, after)
        athlete_id = r[0].athlete.id
        b = Buckets()
        file = 'summary/%s/%s/%s/raw.json' % (athlete_id, before, after)
        b.createFromString(file, str(r).encode())

    def test_storage_insert_collect(self):
        before = 1587730062
        after = 1577922712
        activity = Activity(get_test_access())
        r = activity.get_activity(before, after)
        si = StorageInsert(get_test_access())
        prefix = si.buildSummaryPrefix(before, after, r)
        si.insert_all_from_summary(r)
