
from flask_restful import Resource
from flask import jsonify, request
import re

from ..models.user_model import UserModel

email_f = r"(^[a-zA-z0-9_.]+@[a-zA-z0-9-]+\.[a-z]+$)"

class Register(Resource ,UserModel):
    """This class provides access to  """
    
    def __init__(self):
        self.data = UserModel()


    def post(self):
        """This method creates a new user"""

        details = request.get_json()
        firstname = details['firstname']
        lastname = details['lastname']
        othername = details['othername']
        email = details['email']
        phonenumber = details['phonenumber']
        username = details['username']
        password = details['password']

        if firstname=="" or email=="" or username =="":
            return {"message":"You must provide all user details",
                    "status":400
                    },400
        if not re.match(email_f,email):
            return{"Message":"You must provide a valid email adress",
                   "Status":400
                  },400

        response = self.data.get_single_user(email)
        if len(response) > 0:
            return {"Message": "User already exists"}  

        else:
            resp = self.data.save(firstname,lastname,othername,email,phonenumber,username,password)
            return {
                "status": 201,
                "data": [
                    {
                        "id": len(resp),
                        "message": "A new user has been created"
                     }
                ]
            },201


