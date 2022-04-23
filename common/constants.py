"""configurations"""
import os
APP_SECRET_KEY = "<!@pp$e(ReT#&*!>"
API_SUCCESS_STATUS = "OK"
API_ERROR_STATUS = "Error"
MONGO_URI = os.environ.get("MONGO_URI")

DB_NAME = os.environ.get("DB_NAME")
TWILIO_WHATSAPP_NUMBER = os.environ.get("TWILIO_WHATSAPP_NUMBER")
TWILIO_API_KEY = os.environ.get("TWILIO_API_KEY")
TWILIO_SID = os.environ.get("TWILIO_SID")

