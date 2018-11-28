
from flask_restful import Resource
from flask import jsonify, request

from ..models.incident_model import IncidentModel

class Incident(Resource ,IncidentModel):
    """This class provides access to operations on Get records """
    
    def __init__(self):
        self.data = IncidentModel()


    def get(self):
        """This method Fetches all records"""

        resp = self.data.get_all_records()
        return jsonify({
            "status": 200,
            "Data": resp
            })
