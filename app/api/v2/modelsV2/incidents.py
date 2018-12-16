import psycopg2
import os
import re
from db.db_config import init_db,close_connection
from flask import jsonify, request
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)

location_format = r"(^([-+]?\d{1,2}([.]\d+)?),\s*([-+]?\d{1,3}([.]\d+)?)$)"

class Record():
    
    def validate_location(self, location):
        """This method validates location coordinates"""
        if not re.match(location_format, location):
            return {"message": "Location does not exist"}
        return True  

    @jwt_required
    def add_record(self,flag_type,location,comment):
        """This method adds a new record(redflag/interventions)"""

        valid_location = self.validate_location(location)
        if valid_location is not True:
            return valid_location
        
        current_user = get_jwt_identity()

        try:
            con = init_db()
            cur = con.cursor()
            cur.execute("SELECT user_id FROM users WHERE email = %s",(current_user,))
            user = cur.fetchone() 
            user_id = user[0]

            cur.execute(
                    "INSERT INTO incidents(type,location,comment,user_id)\
                     VALUES (%s,%s,%s,%s) RETURNING incident_id,type,location,\
                     status,comment,user_id",
                    (flag_type,location,comment,user_id))
            incident = cur.fetchone() 

            new_record = {
                  "Created by":incident[5],
                  "Incident Id":incident[0],
                  "Type":incident[1],
                  "Location":incident[2],
                  "Status":incident[3],
                  "Comment":incident[4]
            }
            close_connection(con)
            return {
                    "status": 201,
                    "message": "Created record successfully",
                    "Data": new_record
                },201               

        except (Exception,psycopg2.DatabaseError) as error:
            print(error)
            return{
                "message":"Error while saving record. Please try again"
            }

    @jwt_required
    def get_record(self):
        """This methods gets all records"""
        try:
            con = init_db()
            cur = con.cursor()
            cur.execute("SELECT incident_id, type,location,status,comment, user_id  FROM incidents")
            data = cur.fetchall() 
            close_connection(con)

            if not data:
                return{
                    "Status": 404,
                    "Message": "There are no records"
                },404
            incidents = []

            for incident in data:
                incident_dict = {
                    "incident_id": incident[0],
                    "flag_type": incident[1],
                    "loction": incident[2],
                    "status": incident[3],
                    "comment": incident[4],
                    "created_by": incident[5]
                    }
                incidents.append(incident_dict)
            return {
                "status": 200,
                "Data":incidents
                }               
        except (Exception,psycopg2.DatabaseError) as error:
            print(error)
            return{
                "message":"Can not get any records"
            }

    @jwt_required
    def get_single_record(self,id):
        """This methods gets all records"""
        try:
            con = init_db()
            cur = con.cursor()
            cur.execute("SELECT incident_id, type,location,status,comment, user_id\
              FROM incidents WHERE incident_id = %s", (id,))
            data = cur.fetchall() 
            close_connection(con)

            if not data:
                return{
                    "Status": 404,
                    "Message": "Record does not exist"
                },404
            incidents = []

            for incident in data:
                incident_dict = {
                    "incident_id": incident[0],
                    "flag_type": incident[1],
                    "loction": incident[2],
                    "status": incident[3],
                    "comment": incident[4],
                    "created_by": incident[5]
                    }
                incidents.append(incident_dict)
            return {
                "status": 200,
                "Data":incidents
                }              
        except (Exception,psycopg2.DatabaseError) as error:
            print(error)
            return{
                "message":"Can not get any records"
            }

    @jwt_required
    def remove_record(self, id):
        """This method deletes a record for the user currently logged in"""

        current_user = get_jwt_identity()
        try:
            con = init_db()
            cur = con.cursor()
            cur.execute("SELECT user_id FROM users WHERE email = %s",(current_user,))
            user = cur.fetchall() 
            user_id = user[0][0]
            cur.execute("SELECT user_id,status FROM incidents WHERE incident_id = %s",(id,))
            user_1 = cur.fetchall()

            if not user_1:
                return{
                    "Status": 404,
                    "Message": "Record does not exist"
                },404

            user_id_1 = user_1[0][0]
            if user_id != user_id_1:
                return{
                    "Status":403,
                    "Message": "Unauthorized request. Can not delete record"
                      },403

            status_type = user_1[0][1]
            if status_type != "Draft":
                return{
                        "Message":"Record in processing.Can not be deleted"
                       }

            cur.execute("DELETE FROM incidents WHERE incident_id = %s", (id,))
            close_connection(con)
            return{
                "Status": 200,
                "Message":"Record has been deleted successfully"
                },200
        except (Exception,psycopg2.DatabaseError) as error:
            print(error)
            return{
                "message":"Record has not been deleted please try again"
            } 

    @jwt_required
    def edit_comment(self,id,comment):
        """This method edits a single location in a record"""

        current_user = get_jwt_identity()
        try:
            con = init_db()
            cur = con.cursor()
            cur.execute("SELECT user_id FROM users WHERE email = %s",(current_user,))
            user = cur.fetchall() 
            user_id = user[0][0]

            cur.execute("SELECT user_id,status FROM incidents WHERE incident_id = %s",(id,))
            user_1 = cur.fetchall()

            if not user_1:
                return{
                    "Status": 404,
                    "Message": "Record does not exist"
                },404

            user_id_1 = user_1[0][0]
            if user_id != user_id_1:
                return{
                    "Status":403,
                    "Message": "Unauthorized request. Can not edit record"
                      },403
            status_type = user_1[0][1]
            if status_type != "Draft":
                return{
                        "Message":"Record in processing.Comment can not be updated"
                       }                      
            cur.execute("UPDATE incidents SET comment = %s WHERE incident_id = %s\
             RETURNING incident_id,type,location,status,comment,user_id",(comment,id))
            updated_record = cur.fetchone()

            new_record = {
                  "Created by":updated_record[5],
                  "Incident Id":updated_record[0],
                  "Type":updated_record[1],
                  "Location":updated_record[2],
                  "Status":updated_record[3],
                  "Comment":updated_record[4]
            }
            close_connection(con)
            return{
                "Status": 200,
                "Message":"Comment updated successfully",
                "Data": new_record               
            }
        except (Exception,psycopg2.DatabaseError) as error:
            print(error)
            return{
                "message":"Record has not been edited please try again"
            } 


    @jwt_required
    def edit_location(self,id,location):
        """This method edits a single location in a record"""

        valid_location = self.validate_location(location)
        if valid_location is not True:
            return valid_location

        current_user = get_jwt_identity()
        try:
            con = init_db()
            cur = con.cursor()
            cur.execute("SELECT user_id FROM users WHERE email = %s",(current_user,))
            user = cur.fetchall() 
            user_id = user[0][0]

            cur.execute("SELECT user_id,status FROM incidents WHERE incident_id = %s",(id,))
            user_1 = cur.fetchall()
            #print(user_1)

            if not user_1:
                return{
                    "Status": 404,
                    "Message": "Record does not exist"
                },404

            user_id_1 = user_1[0][0]
            #print(user_id_1)
            if user_id != user_id_1:
                return{
                    "Status":403,
                    "Message": "Unauthorized request. Can not edit record"
                      },403
            status_type = user_1[0][1]
            print(status_type)
            if status_type != "Draft":
                return{
                        "Message":"Record in processing.Location can not be updated"
                       }                      
            cur.execute("UPDATE incidents SET location = %s WHERE incident_id = %s\
             RETURNING incident_id,type,location,status,comment,user_id",(location,id))
            updated_record = cur.fetchone()
            new_record = {
                  "Created by":updated_record[5],
                  "Incident Id":updated_record[0],
                  "Type":updated_record[1],
                  "Location":updated_record[2],
                  "Status":updated_record[3],
                  "Comment":updated_record[4]
            }
            close_connection(con)
            return{
                "Status": 200,
                "Message":"Location updated successfully",                
                "Data": new_record
            }
        except (Exception,psycopg2.DatabaseError) as error:
            print(error)
            return{
                "message":"Record has not been edited please try again"
            } 