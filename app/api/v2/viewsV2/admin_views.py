from flask import jsonify, request
from flask_restful import Resource
from ..modelsV2.admin_models import Status

class StatusV(Resource,Status):
    
    def __init__(self):
        self.data = Status()

    def patch(self,type,id):
        """edit a status"""
        details = request.get_json()
        status = details['status']

        if not status:
            return{
                "Status": 400,
                "Message": "Please enter required details"
            },400

        return self.data.edit_status(id,type,status)