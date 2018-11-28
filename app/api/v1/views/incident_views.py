
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

    def post(self):
        """This method creates a new record"""

        details = request.get_json()
        createdBy = details['createdBy']
        record_type = details['type']
        location = details['location']
        comment = details['comment']

        resp = self.data.save(createdBy,record_type,location,comment)
        id = resp[0]['id']
        return jsonify({
            "Status": 201,
             "data":[{
                  "id" : id,  
                  "message": "created record Successfully"
                 }]
             })


class SingleRecord(Resource, IncidentModel):
     """This resource will be used to get a single record """

     def __init__(self):
        self.db = IncidentModel()

     def get(self,id):
         """This method gets a single incident record"""

         if not id or not isinstance(id,int):
             return jsonify({
                 "Status": 404,
                 "Message": "Please Enter a valid ID"
             })

         resp = self.db.get_single_record(id)
         if len(resp)== 0:
             return jsonify({
                 "Status": 404,
                 "Message": "Record not Found"
             })
         return jsonify({
            "status": 200,
            "Data": resp            
         })


     def delete(self,id):
         """This method delete a record given the Id"""
             
         resp = self.db.get_single_record(id)

         if len(resp)==0:
             return jsonify({
                 "message": "No record with this ID", 
                 "status": 404})
          
         status = resp [0]['status']
         id = resp [0]['id']

         if status == "Draft":
             resp = self.db.delete_record(id)
             return jsonify({
                 "Status": 200,
                 "Data": [{
                     "id": id,
                     "Message": "Record deleted successfully"
                 }]
             })
         return jsonify({
             "Status": 400,
             "Message": "Record can not be deleted"
         })

    
