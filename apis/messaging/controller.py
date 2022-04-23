"""database queries."""
import datetime
from master.app import db


def save_message(message: dict):
    """save incomming message in database"""
    db.messages.insert_one({**message, "datetime": datetime.datetime.now()})
