import psycopg2
import os
from db.db_config import init_db,close_connection
from flask import jsonify, request
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)

class Status():
    """This class is for editing status of a record"""

    @jwt_required
    def edit_status(self,id,type,status):
        """This method is for editing the record of a status"""

        current_user = get_jwt_identity()
        try:
            con = init_db()
            cur = con.cursor()
            cur.execute("SELECT is_admin FROM users WHERE email = %s",(current_user,))
            user = cur.fetchall() 
            user_role = user[0][0]  
        
            if user_role != True:
                return{
                    "Status": 403,
                    "Message":"Unauthorized user"            
                      },403 
            cur.execute("SELECT * FROM incidents WHERE \
            incident_id = %s AND type = %s",(id,type))
            record = cur.fetchall()
            if not record:
                return{
                    "Status": 404,
                    "Message": "Record does not exist"
                },404  
            cur.execute("UPDATE incidents SET status = %s WHERE \
            incident_id = %s and type = %s \
            RETURNING incident_id,type,location,status,comment,user_id",
            (status,id,type))
            updated_record = cur.fetchone()
            close_connection(con)
            new_record = {
                  "Created by":updated_record[5],
                  "Incident Id":updated_record[0],
                  "Type":updated_record[1],
                  "Location":updated_record[2],
                  "Status":updated_record[3],
                  "Comment":updated_record[4]
            }
            return{
                "Status": 200,
                "Message":"Updated " + type + " record status",
                "Data": new_record
            }
        except (Exception,psycopg2.DatabaseError) as error:
            print(error)
            return{
                "message":"Record has not been edited please try again"
            }      