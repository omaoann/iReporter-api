import psycopg2
import os
from db.db_config import init_db,close_connection
from flask import jsonify, request
import re
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)

email_format = r"(^[a-zA-z0-9_.]+@[a-zA-z0-9-]+\.[a-z]+$)"

class Users():
    
    def validate_email(self, email):
        """This method validates email addresses"""
        if not re.match(email_format, email):
            return {"message": "Please enter a valid email",
                            "status": 400},400
        return True       
    
    def save_user(self,f_name,o_name,l_name,username,\
                             email,phone_no,password):
        """This method adds a new user during registration"""
        valid_email = self.validate_email(email)
        if valid_email is not True:
            return valid_email

        try:
            con = init_db()
            cur = con.cursor()
            cur.execute("SELECT * FROM users WHERE username = %s OR email = %s",(username,email))
            user_exist = cur.fetchone() 

            if user_exist:
                return{
                    "message": "User already exists",
                    "status": 400
                },400
            else:
                cur.execute(
                    "INSERT INTO users(f_name,o_name,l_name,username,\
                    email,phone_no, password)VALUES (%s,%s,%s,%s,%s,%s,%s) \
                    RETURNING user_id, f_name,l_name,username,email,phone_no",
                    (f_name,o_name,l_name,username,email,phone_no,password))
                user = cur.fetchone() 

                new_user = {
                    "UserId": user[0],
                    "First name": user[1],
                    "Last name": user[2],
                    "Username": user[3],
                    "Email": user[4],
                    "Phone Number": user[5]
                }
                close_connection(con)
                return {
                    "message": "User created successfully.Kindly login",
                    "User": new_user,
                    "status": 201
                },201               

        except (Exception,psycopg2.DatabaseError) as error:
            print(error)
            return{
                "message":"Error while saving user. Please try again"
            }

    def user_login(self, email, password):
        """Method to log in a user"""

        valid_email = self.validate_email(email)
        if valid_email is not True:
            return valid_email

        con = init_db()
        cur = con.cursor()
        cur.execute("SELECT password FROM users WHERE email = %s", (email,))
        user_exists = cur.fetchone()
        close_connection(con)
        if not user_exists:
            return {
                "message": "Wrong email or password",
                "status": 400
            },400

        db_password = user_exists[0]
        if db_password != password:
            return {
                "message": "Wrong email or password",
                "status": 400
            },400
      
        access_token = create_access_token(identity=email)
        return {
            "message": "Successfully logged in",
            "token": access_token,
            "status": 200
        },200
