from flask import jsonify, request
from flask_restful import Resource, reqparse
from ..modelsV2.incidents import Record

parser=reqparse.RequestParser(bundle_errors=True)
parser.add_argument(
    'flag_type',type=str,
       required=True,
       help="Field can not be left blank"
       )
parser.add_argument(
    'location',type=str,
       required=True,
       help="Field can not be left blank"
)
parser.add_argument(
    'comment',type=str,
       required=True,
       help="Field can not be left blank"
       )

class AddRecord(Resource,Record):
    """This class registers a new user"""
    
    def __init__(self):
        self.data = Record()

    def post(self):
        data = parser.parse_args()
        #print(data)
        flag_type = data['flag_type']
        location = data['location']
        comment = data['comment']

        if not comment or not location or not flag_type:
            return {
                "message": "Please fill all fields",
                "status": 400
            },400

        if comment.isspace()==True\
            or location.isspace()==True\
            or flag_type.isspace()==True:
            return {
                "message": "Field can not contain white space",
                "status": 400
            },400

        return self.data.add_record(flag_type,location,comment)

class GetRecords(Resource,Record):
    """This class gets all records"""
    
    def __init__(self):
        self.data = Record()

    def get(self,type):
        """Get all records"""
        return self.data.get_record(type)

class GetRecord(Resource,Record):
    """This class gets a single record and deletes a record"""
    
    def __init__(self):
        self.data = Record()

    def get(self,type,id):
        """Get single record by id"""
        return self.data.get_single_record(id,type)

    def delete(self,type,id):
        """This method deletes a single record"""
        return self.data.remove_record(id,type)

parser_c=reqparse.RequestParser(bundle_errors=True)
parser_c.add_argument(
    'comment',type=str,
       required=True,
       help="Field can not be left blank"
       )
class EditComment(Resource,Record):
    """This class edits a specific comment"""
    
    def __init__(self):
        self.data = Record()

    def patch(self,type,id):
        """edit a comment"""
        details = parser_c.parse_args()
        comment = details['comment']

        if comment=="" or comment.isspace()==True:
            return{
                "Status": 400,
                "Message": "Field can not be empty or contain whitespace"
            },400

        return self.data.edit_comment(id,type,comment)

parser_l=reqparse.RequestParser(bundle_errors=True)
parser_l.add_argument(
    'location',type=str,
       required=True,
       help="Field can not be left blank"
       )
class EditLocation(Resource,Record):
    """This class edits a specific comment"""
    
    def __init__(self):
        self.data = Record()

    def patch(self,type,id):
        """edit a location"""
        details = parser_l.parse_args()
        location = details['location']

        if location=="" or location.isspace()==True:
            return{
                "Status": 400,
                "Message": "Field can not be empty or contain whitespace"
            },400

        return self.data.edit_location(id,type,location)