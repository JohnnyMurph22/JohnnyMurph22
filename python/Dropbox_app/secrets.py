# from urllib import response
# import requests

# response = requests.get('https://www.dropbox.com/oauth2/authorize?client_id=hoy3yclqx1lnq0r&response_type=code')

# print(response.status_code)

# print(response.json())

#!/usr/bin/env python3

import dropbox
from dropbox import DropboxOAuth2FlowNoRedirect

# '''
# This example walks through a basic oauth flow using the existing long-lived token type
# Populate your app key and app secret in order to run this locally
# '''
APP_KEY = "hoy3yclqx1lnq0r"
APP_SECRET = "fz460i8umc716qy"


auth_flow = DropboxOAuth2FlowNoRedirect(APP_KEY, APP_SECRET)

authorize_url = auth_flow.start()
print("1. Go to: " + authorize_url)
print("2. Click \"Allow\" (you might have to log in first).")
print("3. Copy the authorization code.")
auth_code = input("Enter the authorization code here: ").strip()

try:
    oauth_result = auth_flow.finish(auth_code)
except Exception as e:
    print('Error: %s' % (e,))
    exit(1)

with dropbox.Dropbox(oauth2_access_token=oauth_result.access_token) as dbx:
        dbx.users_get_current_account()
        print("Successfully set up client!")
