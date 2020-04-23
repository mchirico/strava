import swagger_client
from swagger_client.api.activities_api import ActivitiesApi  # noqa: E501

from bigQuery.bigQstrava import BQStrava

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


class BigQInsert:

    def insertraw(self, before, after, raw):
        athlete_id = raw[0].athlete.id

        bqstrava = BQStrava()
        bqstrava.athlete_raw(athlete_id, before, after, raw)
