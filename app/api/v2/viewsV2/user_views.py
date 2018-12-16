from flask import jsonify, request
from flask_restful import Resource, reqparse
from ..modelsV2.users import Users

parser=reqparse.RequestParser(bundle_errors=True)
parser.add_argument(
    'firstname',type=str,
       required=True,
       help="Firstname field can not be left blank"
       )
parser.add_argument(
    'lastname',type=str,
       required=True,
       help="Last name field can not be left blank"
       )
parser.add_argument(
    'othername',type=str,
       required=True,
       help="Other name field can not be left blank"
       )       
parser.add_argument(
    'username',type=str,
       required=True,
       help="Username field can not be left blank"
       )
parser.add_argument(
    'email',type=str,
       required=True,
       help="Username field can not be left blank"
       )
parser.add_argument(
    'phonenumber',type=int,
       required=True,
       help="Phone number field can not be left blank"
       )   
parser.add_argument(
    'password',type=str,
       required=True,
       help="Password field can not be left blank"
       )    

class Register(Resource):
    """This class registers a new user"""
    
    def __init__(self):
        self.data = Users()

    def post(self):
        details = parser.parse_args()
        f_name = details['firstname']
        l_name = details['lastname']
        o_name = details['othername']
        username = details['username']
        email = details['email']
        phone_no = details['phonenumber']
        password = details['password']

        if not email or not password or not f_name\
         or not phone_no or not f_name or not l_name\
         or not o_name:
            return {
                "message": "Please fill all required fields",
                "status": 400
            },400
        if f_name.isalpha() is False:
            return {'message': 'Please enter a valid First name'}, 400
        if l_name.isalpha() is False:
            return {'message': 'Please enter a valid Last name'}, 400
        if o_name.isalpha() is False:
            return {'message': 'Please enter a valid other name'}, 400

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