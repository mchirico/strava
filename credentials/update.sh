#!/bin/bash
# This uploads, assuming you have secret files locally
# You can keep this is repo, to show where files are located.
gsutil cp __init__.py gs://nodesepta/strava/credentials/__init__.py
gsutil cp creds.py gs://nodesepta/strava/credentials/creds.py
gsutil cp firebase.json gs://nodesepta/strava/credentials/firebase.json
gsutil cp update.sh gs://nodesepta/strava/credentials/update.sh
gsutil cp bigquery.json gs://nodesepta/strava/credentials/bigquery.json
