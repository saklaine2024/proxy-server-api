import firebase_admin
from firebase_admin import credentials, auth, firestore

# Initialize Firebase Admin SDK
def initialize_firebase():
    # Path to your Firebase service account credentials JSON file
    cred = credentials.Certificate('firebase-admin-sdk.json')  # Replace with actual path
    firebase_admin.initialize_app(cred)

# Function to verify Firebase ID token
def verify_token(id_token):
    try:
        decoded_token = auth.verify_id_token(id_token)
        return decoded_token
    except Exception as e:
        return {"error": str(e)}

# Access Firestore database
def get_firestore_client():
    db = firestore.client()
    return db
