from flask import jsonify, request
from flask_restful import Resource
from ..modelsV2.users import Users

class Register(Resource):
    """This class registers a new user"""
    
    def __init__(self):
        self.data = Users()

    def post(self):
        details = request.get_json()
        f_name = details['firstname']
        l_name = details['lastname']
        o_name = details['othername']
        username = details['username']
        email = details['email']
        phone_no = details['phonenumber']
        password = details['password']

        if not email or not password or not f_name or not phone_no:
            return {
                "message": "Please fill all fields",
                "status": 400
            },400

        return self.data.save_user(f_name,o_name,l_name,username,\
                     email,phone_no,password)


class Login(Resource):
    """This class enables user login"""

    def __init__(self):
        self.data = Users()

    def post(self):
        details = request.get_json()
        email = details['email']
        password = details['password']

        if not password or not email:
            return{
                "message":"Please fill all fields",
                "status":"400"
            },400

        return self.data.user_login(email,password)