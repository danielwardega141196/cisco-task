from flask import Flask, jsonify, make_response
from flask_swagger_ui import get_swaggerui_blueprint
from routes.api import API

APP = Flask(__name__)


SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    base_url=SWAGGER_URL,
    api_url=API_URL,
    config={
        'app_name': "Seans-Python-Flask-REST-Boilerplate"
    }
)
APP.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
APP.register_blueprint(API)


if __name__ == '__main__':
    APP.run(debug=False)
