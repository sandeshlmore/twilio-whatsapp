
import structlog
from flask import make_response, jsonify
from flask_restful import Resource

from common.constants import API_SUCCESS_STATUS
from master.app import api
from flask import Blueprint

health_blueprint = Blueprint('health', __name__)
logger = structlog.get_logger()


class Health(Resource):
    def get(self):
        """This endpoint takes user message from twilio and reply it back to the same user."""
        return make_response(jsonify({'status': API_SUCCESS_STATUS, 'online': "true"}), 200)


api.add_resource(Health, '/health-check')
