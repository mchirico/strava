import requests


class Stream:

    def __init__(self, access_token):
        self.access_token = access_token

    def get_stream(self, id):
        self.id = id
        url = "https://www.strava.com/api/v3/activities/{}/streams?keys=time," \
              "heartrate,altitude,cadence," \
              "temp,velocity_smooth,moving&key_by_type=true&access_token={}".format(
            id, self.access_token)
        r = requests.get(url)
        return r.json()
