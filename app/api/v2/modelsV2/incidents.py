import psycopg2
import os
from db.db_config import init_db,close_connection
from flask import jsonify, request
import re
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
                     VALUES (%s,%s,%s,%s) RETURNING incident_id",
                    (flag_type,location,comment,user_id))
            incident = cur.fetchone() 

            new_record = incident[0]
            close_connection(con)
            return {
                    "status": 201,
                    "Data":[{
                        "message": "Created record successfully",
                        "Id": new_record
                    }]
                },201               

        except (Exception,psycopg2.DatabaseError) as error:
            print(error)
            return{
                "message":"Error while saving record. Please try again"
            }