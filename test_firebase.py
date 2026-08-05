from firebase_config import db

doc = {
    "name": "Bhavana",
    "project": "KS Xerox"
}

db.collection("test").add(doc)

print("✅ Firebase Connected Successfully!")