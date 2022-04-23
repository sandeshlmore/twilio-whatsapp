import certifi
from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from pymongo import MongoClient

from common.constants import MONGO_URI, DB_NAME, APP_SECRET_KEY, TWILIO_SID, TWILIO_API_KEY
from twilio.rest import Client


def create_app():
    """create flask app instance"""
    app = Flask(__name__)
    app.config['SECRET_KEY'] = APP_SECRET_KEY
    CORS(app, resources={r"*": {"origins": "*"}})
    return app


def create_db():
    """create mongo db connection"""
    mongo = MongoClient(MONGO_URI, connect=False, tlsCAFile=certifi.where())
    db = mongo[DB_NAME]
    return db


app = create_app()
db = create_db()
api = Api(app)
twilio_client = Client(TWILIO_SID, TWILIO_API_KEY)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=False, threaded=True)
