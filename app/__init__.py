from flask import Flask, Blueprint
from flask_jwt_extended import JWTManager

from instance.config import app_config
from .api.v1 import version_one as v1
from .api.v2 import version_two as v2
from db.db_config import create_tables, drop_tables,create_default_admin

def create_app(config_name):
    app = Flask(__name__)
    create_tables()
    create_default_admin()

    jwt = JWTManager(app)
    app.config['JWT_SECRET_KEY'] = 'ireportersecret' 

    app.url_map.strict_slashes = False
    
    app.register_blueprint(v1)
    app.register_blueprint(v2)

    return app