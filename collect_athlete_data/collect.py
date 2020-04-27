import swagger_client
from swagger_client.api.activities_api import ActivitiesApi  # noqa: E501
import logging
from bigQuery.bigQstrava import BQStrava

from storage.storage import Buckets
from streams.streams import Stream

configuration = swagger_client.Configuration()


class Activity:

    def __init__(self, access_token):
        configuration.access_token = access_token
        self.api = swagger_client.api.activities_api.ActivitiesApi(
            swagger_client.ApiClient(configuration))

    def get_activity(self, before, after):
        self._ajson = self.api.get_logged_in_athlete_activities(before=before,
                                                                after=after)
        return self._ajson


class StorageInsert:

    def __init__(self, access_token):
        self.b = Buckets()
        configuration.access_token = access_token
        self.api = swagger_client.api.activities_api.ActivitiesApi(
            swagger_client.ApiClient(configuration))
        self.stream = Stream(access_token)

    def buildSummaryPrefix(self, before, after, r):
        athlete_id = r[0].athlete.id
        self._summary_prefix = 'summary/%s/%s/%s/raw.json' % (
            athlete_id, before, after)
        return self._summary_prefix

    def checkExist(self, prefix):
        r = self.b.list(prefix)
        if len(r) > 0:
            return True
        return False

    def insert_all_from_summary(self, r):
        athlete_id = r[0].athlete.id
        for row in r:
            logging.warning("row:{}".format(row.id))
            id = row.id
            json = self.api.get_activity_by_id(id, include_all_efforts=True)
            file = 'event/%s/%s/raw.json' % (athlete_id, id)
            self.b.createFromString(file, str(json).encode())

            file = 'event/%s/%s/laps.json' % (athlete_id, id)
            json = self.api.get_laps_by_activity_id(id)
            self.b.createFromString(file, str(json).encode())

            file = 'event/%s/%s/stream.json' % (athlete_id, id)
            json = self.stream.get_stream(id)
            self.b.createFromString(file, str(json).encode())


class BigQInsert:

    def insertraw(self, before, after, raw):
        athlete_id = raw[0].athlete.id

        bqstrava = BQStrava()
        bqstrava.athlete_raw(athlete_id, before, after, raw)

    def summary(self, raw):
        bqstrava = BQStrava()
        bqstrava.athlete_summary(raw)
        query = """
                insert into `septapig.strava.summary`
        SELECT distinct b.* FROM `septapig.strava.summary` a
        RIGHT OUTER join  `septapig.strava.summary_tmp` b
        on a.id = b.id and a.start = b.start
        where a.id is null
                """
        bqstrava.select(query)

