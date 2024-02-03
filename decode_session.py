from base64 import b64decode
from itsdangerous import TimestampSigner
from itsdangerous.url_safe import URLSafeTimedSerializer
import json
from os import environ as env
from dotenv import find_dotenv, load_dotenv

ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)


# Your secret key used in SessionMiddleware
secret_key = env.get("APP_SECRET_KEY")

# The session cookie value you want to decode
session_cookie_value = "<ADD SESSION HERE>"

# Create a serializer instance with your secret key
serializer = TimestampSigner(secret_key)

# Decrypt and deserialize the session cookie
try:
    # Decrypt the session cookie value
    data = serializer.unsign(session_cookie_value)
    decrypted_value = json.dumps(b64decode(data).decode("utf-8"))
    
    # Deserialize the session data (assuming JSON format)
    session_data = json.loads(decrypted_value)
    
    print("Decoded session data:", session_data)
except Exception as e:
    print(f"Error decoding session cookie: {e}")
