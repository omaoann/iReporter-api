from .views.incident_views import Incident, SingleRecord, EditComment, EditLocation 

from flask_restful import Api, Resource
from flask import Blueprint


version_one = Blueprint('api_v1',__name__,url_prefix='/api/v1/')
api = Api(version_one)

api.add_resource(Incident, 'red-flags')
api.add_resource(SingleRecord, 'red-flags/<int:id>')
api.add_resource(EditComment, 'red-flags/<int:id>/comment')
api.add_resource(EditLocation, 'red-flags/<int:id>/location')