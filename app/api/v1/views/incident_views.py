
from flask_restful import Resource
from flask import jsonify, request

from ..models.incident_model import IncidentModel, incidents

class Incident(Resource ,IncidentModel):
    """This class provides access to operations on Get and post records """
    
    def __init__(self):
        self.data = IncidentModel()


    def get(self):
        """This method Fetches all records"""

        resp = self.data.get_all_records()
        if len(resp)== 0:
             return {
                 "Status": 404,
                 "Message": "No records found"
             },404
        return {
            "status": 200,
            "Data": resp
            },200

    def post(self):
        """This method creates a new record"""

        details = request.get_json()
        createdBy = details['createdBy']
        record_type = details['type']
        location = details['location']
        comment = details['comment']

        if not comment or comment=="" or not location :
            return {"message":"You must provide record details",
                    "status":400
                    },400

        resp = self.data.save(createdBy,record_type,location,comment)
        return {
                "status": 201,
                "data": [
                    {
                        "id": len(resp),
                        "message": "created red-flag record"
                     }
                ]
            },201


class SingleRecord(Resource, IncidentModel):
    """This resource will be used to get a single record """

    def __init__(self):
        self.db = IncidentModel()

    def get(self,id):
        """This method gets a single incident record"""

        if not id or not isinstance(id,int):
            return {
                "Status": 404,
                "Message": "Please Enter a valid ID"
            },404

        resp = self.db.get_single_record(id)
        if len(resp)== 0:
            return {
                "Status": 404,
                "Message": "Record not Found"
            },404
             
        return {
            "status": 200,
            "Data": resp            
        },200


    def delete(self,id):
        """This method deletes a record"""
        record = self.get_single_record(id)
        if len(record) == 0:
            return {"message": "No record with this ID", "status": 404},404
        incidents.remove(record[0])
        return {
                "status": 200,
                "data": [
                    {
                        "id": id,
                        "message": "Red-flag record has been deleted"
                    }
                ]
            },200

class EditComment(Resource, IncidentModel):
    """This resource will be used to edit a comment"""

    def __init__(self):
        pass

    def patch(self,id):
        """ This method updates the comment field data"""
        resp = self.get_single_record(id)

        if len(resp) == 0:

            return jsonify({
                "message": "No record with this ID", 
                "status": 404
               })

        data = request.get_json()

        comment = data['comment']

        index = self.get_index(id)
        data = {
            "comment": comment,
            "index": index
        }

        self.update_comment(**data)
        return jsonify({
            "status": 200,
            "data":[{
                "id": id,
                "message": "Updated red-flag record's Comment"
            }]
            })   


class EditLocation(Resource, IncidentModel):
    """This resource will be used to edit location of a record"""

    def __init__(self):
        pass

    def patch(self,id):
        """Updates record location data"""
        resp = self.get_single_record(id)

        if len(resp) == 0:

            return jsonify({
                "message": "No record with this ID", 
                "status": 404
               })

        data = request.get_json()

        location = data['location']

        index = self.get_index(id)
        data = {
            "location": location,
            "index": index
        }
        
        self.update_location(**data)
        return jsonify({
            "status": 200,
            "data":[{
                "id": id,
                "message": "Updated red-flag record's Location"
            }]
            })   
