import traceback

import structlog
from flask import make_response, jsonify, request
from flask_restful import Resource

from apis.messaging.controller import save_message
from common.constants import API_SUCCESS_STATUS, TWILIO_WHATSAPP_NUMBER, API_ERROR_STATUS
from master.app import api, twilio_client
from flask import Blueprint

message_blueprint = Blueprint('messaging_blueprint', __name__)
logger = structlog.get_logger()


class TwilioWebhook(Resource):
    def post(self):
        """This endpoint takes user message from twilio and reply it back to the same user."""
        from_number = request.values.get("From")
        text_message = request.values.get("Body")
        log = logger.bind(mid=request.values.get("MessageSid"))
        media = {}
        if int(request.values.get("NumMedia", 0)):
            media = {
                "media": request.values.get("MediaUrl0", 1),
                "media_type": request.values.get("MediaContentType0")
            }
        message = {"from": from_number, "text": text_message, "to": TWILIO_WHATSAPP_NUMBER, **media}
        log.info("Incoming Message", message=message)
        try:
            save_message(message)

            twilio_client.messages.create(from_='whatsapp:'+TWILIO_WHATSAPP_NUMBER,
                                          to=from_number,
                                          body="You sent: " + text_message,
                                          media_url=media.get("media"))
            return make_response(jsonify({'status': API_SUCCESS_STATUS, 'message': "Reply Sent Successfully."}), 200)
        except Exception as e:
            twilio_client.messages.create(from_='whatsapp:' + TWILIO_WHATSAPP_NUMBER,
                                          to=from_number,
                                          body="Something went wrong. You can only send text, image, audio, video,"
                                               " contact.")
            log.error("Error while replying to incoming message.", error=e)
            return make_response(jsonify({'status': API_ERROR_STATUS, 'message': str(e)}), 500)


api.add_resource(TwilioWebhook, '/webhook/dummy-reply')
