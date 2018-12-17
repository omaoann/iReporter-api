import unittest
from flask import json
from app import create_app, create_tables, drop_tables, create_default_admin
from .data import (registration_data, empty_reg_data, 
           reg_invalid_email, login_empty_field,login_invalid_name,
           data_login,invalid_password,login_invalid_email,
           reg_whitespace_field,reg_nonstring_field)

class Registration(unittest.TestCase):
    """This class tests for user registration and login"""
    drop_tables()

    def setUp(self):
        """ Define tests variables"""
        create_tables()
        create_default_admin()        
        self.app = create_app(config_name='testing')
        self.client = self.app.test_client()


    def test_user_registered(self):
        response = self.client.post("api/v2/auth/signup", 
                data=json.dumps(registration_data),content_type='application/json')
        result = json.loads(response.data)   
        self.assertEqual(201, response.status_code)  
        self.assertEqual(result['message'],'User created successfully.Kindly login')  


    def test_empty_field(self):
        response = self.client.post("api/v2/auth/signup", 
                data=json.dumps(empty_reg_data),content_type='application/json')
        result = json.loads(response.data)  
        self.assertEqual(result['message'],'Please fill all required fields')     
        self.assertEqual(400, response.status_code)
        

    def test_email_exist(self):
        response = self.client.post("api/v2/auth/signup", 
                data=json.dumps(registration_data),
                content_type="application/json")  
        self.assertEqual(201, response.status_code)  

        response1 = self.client.post("api/v2/auth/signup", 
                data=json.dumps(registration_data),
                content_type='application/json') 
        result = json.loads(response1.data)  
        self.assertEqual(result['message'], "User already exists")
        

    def test_username_exist(self):
        response = self.client.post("api/v2/auth/signup", 
                data=json.dumps(registration_data),
                content_type='application/json')   
        self.assertEqual(201, response.status_code)

        response1 = self.client.post("api/v2/auth/signup", 
                data=json.dumps(registration_data),
                content_type='application/json') 
        result = json.loads(response1.data)  
        self.assertEqual(result['message'], "User already exists")

    def test_email_is_invalid(self):
        response = self.client.post("/api/v2/auth/signup", 
                data=json.dumps(reg_invalid_email),
                                content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(result['message'], "Please enter a valid email")
        self.assertEqual(response.status_code, 400)  
        
    def test_user_signup_with_non_string(self):
        response = self.client.post("/api/v2/auth/signup", 
                data=json.dumps(reg_nonstring_field),
                                content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(result['message'], "Please enter a valid First name")
        self.assertEqual(response.status_code, 400)

    def test_for_whitespace_in_user_registration_input(self):
        response = self.client.post("/api/v2/auth/signup", 
                data=json.dumps(reg_whitespace_field),
                                content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(result['message'], "Field can not contain white space")
        self.assertEqual(response.status_code, 400)                  



############Login Tests###############

    def test_user_login(self):
        response = self.client.post("api/v2/auth/signup", 
                data=json.dumps(registration_data),
                content_type="application/json")           
        self.assertEqual(response.status_code,201)

        response1 = self.client.post("api/v2/auth/login",
                data=json.dumps(data_login), 
                content_type="application/json")
        result = json.loads(response1.data)
        self.assertEqual(response1.status_code,200)
        self.assertEqual(result['message'],"Successfully logged in")

    def test_unregistered_user(self):
        response = self.client.post("api/v2/auth/login",
            data = json.dumps(login_invalid_name),content_type="application/json")
        result = json.loads(response.data)
        self.assertEqual(response.status_code,400)
        self.assertEqual(result["message"],"Wrong email or password")

    def test_wrong_password(self):
        response = self.client.post("api/v2/auth/signup", 
                data=json.dumps(registration_data),content_type="application/json")           
        self.assertEqual(response.status_code,201)

        response1 = self.client.post("api/v2/auth/login",
                data=json.dumps(invalid_password), content_type="application/json")
        result = json.loads(response1.data)
        self.assertEqual(response1.status_code,400)
        self.assertEqual(result["message"],"Wrong email or password")

    def test_invalid_login_email(self):
        response = self.client.post("api/v2/auth/login",
            data = json.dumps(login_invalid_email),content_type="application/json")
        result = json.loads(response.data)
        self.assertEqual(response.status_code,400)
        self.assertEqual(result["message"],"Please enter a valid email")

    def test_empty_login_field(self):
        response = self.client.post("api/v2/auth/login", 
                data=json.dumps(login_empty_field),content_type='application/json')
        result = json.loads(response.data)  
        self.assertEqual(result['message'],'Please fill all fields')     
        self.assertEqual(400, response.status_code)
    

    def tearDown(self):
        drop_tables()