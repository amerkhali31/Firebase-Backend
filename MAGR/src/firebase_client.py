from firebase_admin import initialize_app, firestore
import os

# Set the environment variable firebase looks for to properly configure app for correct database
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "MAGR/magr-7ae80-firebase-adminsdk-kt2vv-a1b50163e3.json"

app = initialize_app()
db = firestore.client()