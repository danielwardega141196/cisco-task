from unittest.mock import patch
from routes.api import API, info
from routes.constants import INFO_RESPONSE
import http.client


@patch.object(API, "route", lambda item: item)
def test_info():
    assert info() == (INFO_RESPONSE, http.client.OK)





