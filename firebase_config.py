import os
import firebase_admin
from firebase_admin import credentials, firestore

firebase_path = os.getenv(
    "GOOGLE_APPLICATION_CREDENTIALS",
    "serviceAccountKey.json"
)

if not firebase_admin._apps:
    cred = credentials.Certificate(firebase_path)
    firebase_admin.initialize_app(cred)

db = firestore.client()