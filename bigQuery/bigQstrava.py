from google.cloud import bigquery
import os
import time
import datetime
import hashlib
from utils.util import findFile

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = findFile("strava.json")
os.environ['TZ'] = 'US/Eastern'
time.tzset()


class BQStrava:

    def __init__(self):
        self.client = bigquery.Client()

    def getTime(self):
        query = "SELECT CURRENT_DATETIME('America/New_York') as now;"
        query_job = self.client.query(query)
        for row in query_job:
            # Row values can be accessed by field name or index.
            return row["now"]

    def select(self, query):
        query_job = self.client.query(query)
        [x for x in query_job]
        return query_job

    def athlete_raw(self, athlete_id, before, after, json):
        table_id = "septapig.strava.activities_raw"
        table = self.client.get_table(table_id)
        time_stamp = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%s")
        h = hashlib.md5(str(json).encode())
        hash = h.digest()
        rows_to_insert = [(athlete_id, before, after, str(json),
                           time_stamp, hash)]
        errors = self.client.insert_rows(table, rows_to_insert)
        print(errors)

    def athlete_summary(self, rows):
        rows_to_insert = []
        for r in rows:
            id = r.id
            start = r.start_date.strftime("%Y-%m-%dT%H:%M:%S.%s")
            stop = r.start_date.strftime("%Y-%m-%dT%H:%M:%S.%s")
            distance = r.distance
            max_speed = r.max_speed
            moving_tine = r.moving_time
            elapsed_time = r.elapsed_time
            average_speed = r.average_speed
            flagged = r.flagged
            name = r.name
            time_stamp = datetime.datetime.now().strftime(
                "%Y-%m-%dT%H:%M:%S.%s")
            athlete = r.athlete.id
            rows_to_insert.append((id, start, stop, distance,
                                   max_speed, moving_tine, elapsed_time,
                                   average_speed, flagged, name,
                                   time_stamp, athlete))

        table_id = "septapig.strava.summary_tmp"
        table = self.client.get_table(table_id)
        errors = self.client.insert_rows(table, rows_to_insert)
        print(errors)
