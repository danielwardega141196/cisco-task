import http.client
from unittest.mock import patch, MagicMock

import routes.api as routes_api
from routes.constants import INFO_RESPONSE


@patch.object(routes_api.API, "route", lambda item: item)
def test_info():
    assert routes_api.info() == (INFO_RESPONSE, http.client.OK)


@patch.object(routes_api.API, "route", lambda item: item)
@patch.object(routes_api, "requests")
@patch.object(routes_api, "flask_request")
@patch.object(routes_api, "_get_payload_error_response")
@patch.object(routes_api, "_prepare_ping_endpoint_response")
def test_ping(
    prepare_ping_endpoint_response,
    payload_error_response,
    flask_request,
    requests_library
):

    example_url_data = {'url': 'example'}
    flask_request.form = example_url_data

    payload_error_response.return_value = False

    requests_library_get_return_value = "requests_library_get_return_value"
    requests_library_get = MagicMock(return_value=requests_library_get_return_value)
    requests_library.get = requests_library_get

    # Execution of the function
    routes_api.ping()

    # check if specified functions has been run with specified parameters
    payload_error_response.assert_called_once_with(payload=example_url_data)
    requests_library_get.assert_called_once_with(example_url_data['url'])
    prepare_ping_endpoint_response.assert_called_once_with(r=requests_library_get_return_value)


