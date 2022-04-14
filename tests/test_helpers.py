from unittest.mock import patch, MagicMock

import requests

import routes.helpers as routes_helpers


def test_prepare_ping_endpoint_response_with_error():

    # prepare custom request
    r = MagicMock()
    error_message = 'test_prepare_ping_endpoint_response_with_error'
    r.raise_for_status = MagicMock(side_effect=requests.exceptions.HTTPError(error_message))
    r.status_code = 400

    # execute function with error and check result
    result = routes_helpers._prepare_ping_endpoint_response(r=r)
    expected_result = {"error_message": error_message}, r.status_code
    assert result == expected_result


def test_prepare_ping_endpoint_response_without_error():

    # prepare custom request
    r = MagicMock()
    r.raise_for_status = MagicMock()
    json_return_value = "json"
    r.json = MagicMock(return_value=json_return_value)
    r.status_code = 200

    # execute function without error and check result
    result = routes_helpers._prepare_ping_endpoint_response(r=r)
    expected_result = {"data": json_return_value}, r.status_code
    assert result == expected_result
    r.raise_for_status.assert_called_once()
    r.json.assert_called_once()


@patch.object(routes_helpers, "create_note_schema")
def test_get_payload_error_response_without_error(create_note_schema):

    # mock validation function
    create_note_schema.validate = MagicMock(return_value=False)

    payload = {}

    # check results
    assert routes_helpers._get_payload_error_response(payload=payload) is None
    create_note_schema.validate.assert_called_once_with(payload)


@patch.object(routes_helpers, "create_note_schema")
def test_get_payload_error_response_with_error(create_note_schema):

    # mock validation function
    create_note_schema.validate = MagicMock(return_value=True)

