import unittest
from flask import json
from app import create_app, create_tables, drop_tables
from .data import *

class Records(unittest.TestCase):
    """This class tests for posting incident data"""
    drop_tables()

    def setUp(self):
        """ Define tests variables"""
        create_tables()
        self.app = create_app(config_name='testing')
        self.client = self.app.test_client()

    def test_create_incidents(self):
        """This method tests for creation of a new incident"""
        response = self.client.post("api/v2/signup", 
                data=json.dumps(registration_data),
                content_type="application/json")           
        self.assertEqual(response.status_code,201)

        response1 = self.client.post("api/v2/login",
                data=json.dumps(data_login), 
                content_type="application/json")
        token = json.loads(response1.data)["token"]

        response2 = self.client.post("api/v2/interventions",
             data=json.dumps(record_data), 
             headers=dict(Authorization='Bearer '+token),
             content_type="application/json")
        result = json.loads(response2.data)
        self.assertEqual(result["Data"][0]["message"],"Created record successfully")
        self.assertEqual(response2.status_code,201)

    def test_empty_field(self):
        """This method tests if a user has left a field empty"""
        response = self.client.post("api/v2/signup", 
                data=json.dumps(registration_data),
                content_type="application/json")           
        self.assertEqual(response.status_code,201)

        response1 = self.client.post("api/v2/login",
                data=json.dumps(data_login), 
                content_type="application/json")
        token = json.loads(response1.data)["token"]

        response2 = self.client.post("api/v2/interventions",
             data=json.dumps(reccord_empty_field), 
             headers=dict(Authorization='Bearer '+token),
             content_type="application/json")
        result = json.loads(response2.data)
        self.assertEqual(result["message"],"Please fill all fields")
        self.assertEqual(response2.status_code,400)

    def test_location_coordinates(self):
        """This method tests if location coordinates are within
                 specified points"""

        response = self.client.post("api/v2/signup", 
                data=json.dumps(registration_data),
                content_type="application/json")           
        self.assertEqual(response.status_code,201)

        response1 = self.client.post("api/v2/login",
                data=json.dumps(data_login), 
                content_type="application/json")
        token = json.loads(response1.data)["token"]

        response2 = self.client.post("api/v2/interventions",
             data=json.dumps(reccord_wrong_location), 
             headers=dict(Authorization='Bearer '+token),
             content_type="application/json")
        result = json.loads(response2.data)
        self.assertEqual(result["message"],"Location does not exist")              

    def tearDown(self):
        drop_tables()