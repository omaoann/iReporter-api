
from flask_restful import Api, Resource
from flask import Blueprint
from .viewsV2.user_views import Register, Login
from .viewsV2.incident_view import (AddRecord,
                        GetRecord,EditComment,EditLocation)
from .viewsV2.admin_views import StatusV


version_two = Blueprint('api_v2',__name__,url_prefix='/api/v2/')
api = Api(version_two)


api.add_resource(Register, 'signup')
api.add_resource(Login, 'login')
api.add_resource(AddRecord, 'interventions')
api.add_resource(GetRecord, 'interventions/<int:id>')
api.add_resource(EditComment, 'interventions/<int:id>/comment')
api.add_resource(EditLocation, 'interventions/<int:id>/location')
api.add_resource(StatusV, '<type>/<int:id>/status')