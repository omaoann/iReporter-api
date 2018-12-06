from flask import Flask, Blueprint

from instance.config import app_config
from .api.v1 import version_one as v1
from .api.v2 import version_two as v2

def create_app(config_name):
    app = Flask(__name__)
    app.register_blueprint(v1)
    app.register_blueprint(v2)

    return app