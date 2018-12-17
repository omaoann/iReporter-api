
from flask_restful import Api, Resource
from flask import Blueprint
from .viewsV2.user_views import Register, Login
from .viewsV2.incident_view import (AddRecord,GetRecords,
                        GetRecord,EditComment,EditLocation)
from .viewsV2.admin_views import StatusV


version_two = Blueprint('api_v2',__name__,url_prefix='/api/v2/')
api = Api(version_two)


api.add_resource(Register, 'auth/signup')
api.add_resource(Login, 'auth/login')
api.add_resource(AddRecord, 'interventions')
api.add_resource(GetRecords, '<type>')
api.add_resource(GetRecord, '<type>/<int:id>')
api.add_resource(EditComment, '<type>/<int:id>/comment')
api.add_resource(EditLocation, '<type>/<int:id>/location')
api.add_resource(StatusV, '<type>/<int:id>/status')