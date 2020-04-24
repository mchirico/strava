from google.cloud import bigquery
import os
import time
from utils.util import findFile

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = findFile("strava.json")
os.environ['TZ'] = 'US/Eastern'
time.tzset()

class BigQ:

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

        """ % (id, ret, msg, self.getTime(), raw, label)

      query_job = self.client.query(query)
      [x for x in query_job]  # Make an API request.
      print("result:", query_job)
      return query_job
      """
