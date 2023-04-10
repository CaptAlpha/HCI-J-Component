# Code to fetch data from google fit and store it in a csv file
#
# Path: SensorConnection\connection.py

import json
import requests
import pandas as pd
import datetime
import time
import os
import numpy as np
import joblib
import requests

from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Set up OAuth 2.0 credentials
scopes = ['https://www.googleapis.com/auth/fitness.activity.read']
flow = InstalledAppFlow.from_client_secrets_file('SensorConnection\client_secret.json', scopes=scopes)
creds = Credentials.from_authorized_user_info(flow.run_local_server()['tokens'])

# Build the Google Fit API client
service = build('fitness', 'v1', credentials=creds)

# Define the data source to fetch data from data.json file
data = json.load(open('data.json'))
data_source = data[0]['dataSourceId']


# Define the time range to fetch data for
start_time = datetime.datetime.utcnow() - datetime.timedelta(days=1)
end_time = datetime.datetime.utcnow()

# Fetch the data from the Google Fit API
data = service.users().dataSources().datasets(). \
    get(userId='me', dataSourceId='derived:com.google.step_count.delta:com.google.android.gms:estimated_steps',
        startTime=start_time.isoformat() + 'Z',
        endTime=end_time.isoformat() + 'Z',
        limit=1000).execute()

# Print the data
print(data)