# coding: utf-8

"""
    Strava API v3

    The [Swagger Playground](https://developers.strava.com/playground) is the
    easiest way to familiarize yourself with the Strava API by submitting
    HTTP requests and observing the responses before you write any client
    code. It will show what a response will look like with different
    endpoints depending on the authorization scope you receive from your
    athletes. To use the Playground, go to
    https://www.strava.com/settings/api and change your “Authorization
    Callback Domain” to developers.strava.com. Please note, we only support
    Swagger 2.0. There is a known issue where you can only select one scope
    at a time. For more information, please check the section “client code”
    at https://developers.strava.com/docs.  # noqa: E501

    OpenAPI spec version: 3.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.activities_api import ActivitiesApi  # noqa: E501
from bigQuery.bigQstrava import BQStrava
from pprint import pprint


from token_utils.token import get_test_access

configuration = swagger_client.Configuration()
configuration.access_token = get_test_access()


# swagger_client.ActivitiesApi(swagger_client.ApiClient(configuration))


class TestActivitiesApi(unittest.TestCase):
    """ActivitiesApi unit test stubs"""

    def setUp(self):
        self.route = swagger_client.RoutesApi(
            swagger_client.ApiClient(configuration))
        self.api = swagger_client.api.activities_api.ActivitiesApi(
            swagger_client.ApiClient(configuration))  # noqa:
        # E501

    def tearDown(self):
        pass

    def test_getActivity(self):
        before = 1587426805  # Integer | An epoch timestamp to use for filtering
        # activities that have taken place before a certain time. (optional)
        after = 1577922712  # Integer | An epoch timestamp to use for filtering

        api_response = self.api.get_logged_in_athlete_activities(before=before,
                                                                 after=after)
        pprint(api_response)

    def test_getActivityBigQ(self):
        before = 1587426805  # Integer | An epoch timestamp to use for filtering
        # activities that have taken place before a certain time. (optional)
        after = 1577922712  # Integer | An epoch timestamp to use for filtering

        api_response = self.api.get_logged_in_athlete_activities(before=before,
                                                                 after=after)

        bq = BQStrava()
        bq.athlete_summary(api_response)
        query = """
        insert into `septapig.strava.summary`
SELECT distinct b.* FROM `septapig.strava.summary` a
RIGHT OUTER join  `septapig.strava.summary_tmp` b
on a.id = b.id and a.start = b.start
where a.id is null
        """
        bq.select(query)




    def test_create_activity(self):
        """Test case for create_activity

        Create an Activity  # noqa: E501
        """
        pass

    def test_get_activity_by_id(self):
        activity_id = 3337410766
        api_response = self.api.get_activity_by_id(activity_id,
                                                   include_all_efforts=True)
        pprint(api_response)

        print('\n\n  --------- \n\n\n')

        # Nice summary ... maybe use
        api_response = self.api.get_laps_by_activity_id(activity_id)
        pprint(api_response)

        # Seems to be similar with above
        api_response = self.api.get_activity_by_id_with_http_info(activity_id)
        pprint(api_response)

        # r = swagger_client.models.detailed_activity.DetailedActivity()
        # pprint(r)
        # TODO: find way to make this work.
        # r = self.route.get_route_as_gpx(3322177112)

        pass

    def test_mytest(self):
        activity_id = 3337410766
        api_response = self.api.get_laps_by_activity_id_with_http_info(
            activity_id)
        pprint(api_response)
        # model = swagger_client.models.altitude_stream.AltitudeStream()  #
        # print(model)
        pass

    def test_get_comments_by_activity_id(self):
        """Test case for get_comments_by_activity_id

        List Activity Comments  # noqa: E501
        """

        # noqa: E501
        pass

    def test_get_kudoers_by_activity_id(self):
        """Test case for get_kudoers_by_activity_id

        List Activity Kudoers  # noqa: E501
        """
        pass

    def test_get_laps_by_activity_id(self):
        """Test case for get_laps_by_activity_id

        List Activity Laps  # noqa: E501
        """
        pass

    def test_get_logged_in_athlete_activities(self):
        """Test case for get_logged_in_athlete_activities

        List Athlete Activities  # noqa: E501
        """
        pass

    def test_get_zones_by_activity_id(self):
        """Test case for get_zones_by_activity_id

        Get Activity Zones  # noqa: E501
        """
        pass

    def test_update_activity_by_id(self):
        """Test case for update_activity_by_id

        Update Activity  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
