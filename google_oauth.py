import json

from google.oauth2.credentials import Credentials

with open('client_secret_oauth.json', 'r') as f:
    creds_data = json.load(f)
    creds = Credentials.from_authorized_user_info(creds_data, 'web')

client_id = creds.client_id
client_secret = creds.client_secret
