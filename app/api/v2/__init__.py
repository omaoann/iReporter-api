
from flask_restful import Api, Resource
from flask import Blueprint
from .viewsV2.user_views import Register, Login


version_two = Blueprint('api_v2',__name__,url_prefix='/api/v2/')
api = Api(version_two)


api.add_resource(Register, 'signup')
api.add_resource(Login, 'login')