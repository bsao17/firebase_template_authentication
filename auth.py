# :param client_secret: Firebase client secret
import os
import firebase_admin
from dotenv import load_dotenv
from firebase_admin import credentials
import pyrebase

load_dotenv()

config = {
    "apiKey": os.getenv('API_KEY'),
    "authDomain": os.getenv('AUTH_DOMAIN'),
    "projectId": os.getenv('PROJECT_ID'),
    "storageBucket": os.getenv('STORAGE_BUCKET'),
    "messagingSenderId": os.getenv('MESSAGING_SENDER_ID'),
    "appId": os.getenv('APP_ID'),
    "measurementId": os.getenv('MEASUREMENT_ID'),
    "databaseURL": ""
}

client_data = {
    "clientId": os.getenv('ID_CLIENT_WEB'),
    "providerId": os.getenv('SECRET_KEY_WEB_CLIENT'),
    "continueUri": "https://example.com/continue",
}

default_app = pyrebase.initialize_app(config)
auth = default_app.auth()
cred = credentials.Certificate('credentials.json')
serverless = firebase_admin.initialize_app(cred)



