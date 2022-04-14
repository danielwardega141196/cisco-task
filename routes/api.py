import http.client

from flask import request as flask_request, Blueprint

from routes.constants import INFO_RESPONSE
from routes.helpers import _get_payload_error_response, _prepare_ping_endpoint_response
import requests


API = Blueprint('api', __name__)


@API.route('/info', methods=['GET'])
def info():
    """
        GET 'info' endpoint which always should return constant
        value of INFO_RESPONSE with the HTTP 200 OK success status
    """
    return INFO_RESPONSE, http.client.OK


@API.route('/ping', methods=['POST'])
def ping():
    """
        POST 'ping' endpoint which ping url specified in payload
    """

    # Get Payload from the request
    payload = flask_request.form

    # Validate payload and return 4XX code if something is wrong
    payload_error_response = _get_payload_error_response(payload=payload)
    if payload_error_response:
        return payload_error_response

    # send the request to the url specified in payload
    url_request = requests.get('http://www.google.com/nothere')

    return _prepare_ping_endpoint_response(r=url_request)
