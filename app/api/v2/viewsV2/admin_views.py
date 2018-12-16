from flask import jsonify, request
from flask_restful import Resource, reqparse
from ..modelsV2.admin_models import Status

parser=reqparse.RequestParser()
parser.add_argument(
    'status',type=str,
       required=True,
       help="Field can not be left blank"
       )

class StatusV(Resource,Status):
    
    def __init__(self):
        self.data = Status()

    def patch(self,type,id):
        """edit a status"""
        data = parser.parse_args()
        #data = request.get_json()
        status = data['status']

        if status.isspace()==True or status=="":
            return{
                "Status": 400,
                "Message": "Field can not contain empty string or whitespace"
            },400

        return self.data.edit_status(id,type,status)