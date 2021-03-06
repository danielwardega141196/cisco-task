import requests
from marshmallow import Schema, fields
import http.client
from typing import Dict, Tuple, Union


class CreateNoteInputSchema(Schema):
    url = fields.Str(required=True)


create_note_schema = CreateNoteInputSchema()


def _get_payload_error_response(payload: Dict) -> Union[None, Tuple]:
    """
         Function prepares error response when payload is incorrect
    """

    payload_errors = create_note_schema.validate(payload)
    if not payload_errors:
        return None

    formatted_payload_error = ", ".join(
        ["'" + key + "'" + ": " + " ".join(value) for key, value in payload_errors.items()]
    )
    error_message = f"There were errors with body: {formatted_payload_error}"
    return error_message, http.client.BAD_REQUEST


def _prepare_ping_endpoint_response(r) -> Dict:
    """
        Function prepares POST 'ping' response
        based on send request
    """
    try:
        r.raise_for_status()
    except requests.exceptions.HTTPError as e:
        return {"error_message": str(e)}, r.status_code
    else:
        return {"data": r.json()},  r.status_code
