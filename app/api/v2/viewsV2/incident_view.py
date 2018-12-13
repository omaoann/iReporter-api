from flask import jsonify, request
from flask_restful import Resource
from ..modelsV2.incidents import Record

class AddRecord(Resource,Record):
    """This class registers a new user and gets all records"""
    
    def __init__(self):
        self.data = Record()

    def post(self):
        details = request.get_json()
        flag_type = details['flag_type']
        location = details['location']
        comment = details['comment']

        if not comment or not location or not flag_type:
            return {
                "message": "Please fill all fields",
                "status": 400
            },400

        return self.data.add_record(flag_type,location,comment)

    def get(self):
        """Get all records"""
        return self.data.get_record()

class GetRecord(Resource,Record):
    """This class gets a single record and deletes a record"""
    
    def __init__(self):
        self.data = Record()

    def get(self,id):
        """Get single record by id"""
        return self.data.get_single_record(id)

    def delete(self,id):
        """This method deletes a single record"""
        return self.data.remove_record(id)

class EditComment(Resource,Record):
    """This class edits a specific comment"""
    
    def __init__(self):
        self.data = Record()

    def patch(self,id):
        """edit a comment"""
        details = request.get_json()
        comment = details['comment']

        if not comment:
            return{
                "Status": 400,
                "Message": "Please enter required details"
            },400

        return self.data.edit_comment(id,comment)

class EditLocation(Resource,Record):
    """This class edits a specific comment"""
    
    def __init__(self):
        self.data = Record()

    def patch(self,id):
        """edit a location"""
        details = request.get_json()
        location = details['location']

        if not location:
            return{
                "Status": 400,
                "Message": "Please enter required details"
            },400

        return self.data.edit_location(id,location)