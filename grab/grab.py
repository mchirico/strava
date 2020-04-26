from collect_athlete_data.collect import Activity, BigQInsert, StorageInsert
import logging

class Grab:

    def __init__(self, access_token, before, after):
        self.access_token = access_token
        self.before = before
        self.after = after

    def bq_insert(self):
        activity = Activity(self.access_token)
        r = activity.get_activity(self.before, self.after)
        bqi = BigQInsert()
        bqi.insertraw(self.before, self.after, r)
        bqi.summary(r)
        return self

    def storage_collect(self):
        logging.warning('here in ')
        activity = Activity(self.access_token)
        r = activity.get_activity(self.before, self.after)
        si = StorageInsert(self.access_token)
        prefix = si.buildSummaryPrefix(self.before, self.after, r)
        si.insert_all_from_summary(r)
        return self
