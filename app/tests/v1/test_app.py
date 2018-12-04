
import unittest
from flask import json

from app import create_app

class Records(unittest.TestCase):
    """Records TestCases Class"""

    def setUp(self):
        """ Define tests variables"""
        self.app = create_app(config_name='testing')
        self.client = self.app.test_client()
        self.data = {
            "createdBy" : "23",
            "type" : "red-flag",
            "location" : "123,345",
            "comment" : "bribe taken"
                }

# tests for user registration
    def test_all_fields_filled(self):
        """Test if it returns error if a field is blank """

        response = self.client.post("api/v1/signup", json={
            "firstname" : "",
            "lastname" : "omao",
            "othername" : "kerubo",
            "email" : "annkay2303@gmail.com",
            "phonenumber" : "0712345678",
            "username" : "annkay",
            "password" : "123456"

        })
        self.assertEquals(400, response.status_code)
        self.assertEquals(response.get_json(), {
            "message":"You must provide all user details", "status": 400
        })

    def test_user_already_exist(self):
        """Test if it alerts user if email already exists"""
        response = self.client.post("api/v1/signup", json={
            "firstname" : "Ann",
            "lastname" : "omao",
            "othername" : "kerubo",
            "email" : "annkay2303@gmail.com",
            "phonenumber" : "0712345678",
            "username" : "annkay",
            "password" : "123456"

        })

        response = self.client.post("api/v1/signup", json={
            "firstname" : "Ann",
            "lastname" : "omao",
            "othername" : "kerubo",
            "email" : "annkay2303@gmail.com",
            "phonenumber" : "0712345678",
            "username" : "annkay",
            "password" : "123456"

        })
        self.assertEquals(response.get_json(),{
                "Message": "User already exists"})
        




# tests for red-flags 
    def test_record_does_not_exist(self):
        """Test for when record does not exist during get"""

        response = self.client.get("/api/v1/red-flags/256")
        self.assertEquals(response.status_code,404)
        self.assertEquals(response.get_json(),{
                "Status": 404,
                "Message": "Record not Found"}
        )

    def test_get_all_records(self):
        """Test if user gets data if there are records"""
        response = self.client.post("/api/v1/red-flags", json=self.data)
        self.assertEquals(response.status_code,201)

        res = self.client.get("/api/v1/red-flags")
        self.assertEquals(res.status_code,200)

    def test_get_single_record(self):
        """Tests if user can get a single record"""

        response = self.client.post("/api/v1/red-flags", json=self.data)
        response = self.client.get("/api/v1/red-flags/1")
        self.assertEquals(response.status_code,200)


    def test_if_id_non_existence_for_get(self):
        """Test for when record does not exist for get"""

        response = self.client.get('/api/v1/red-flags/256')
        self.assertEquals(response.status_code,404)
        self.assertEquals(response.get_json(),{
            "Status": 404,
            "Message": "Record not Found"
                }
        )


    def test_post_record(self):
        """Tests if record posts data"""

        response = self.client.post("/api/v1/red-flags", json=self.data)
        self.assertEquals(response.status_code,201)

    def test_if_user_post_no_comment(self):
        """ test if user leaves out comment section"""

        response = self.client.post("api/v1/red-flags", json={
            "createdBy": "333",
            "type": "red-flag",
            "location": "'-3.7677,0.1234'",
            "comment": ""
        })
        self.assertEquals(400, response.status_code)
        self.assertEquals(response.get_json(), {
            "message":"You must provide record details", "status": 400
        })

    def test_delete_all_records(self):
        """Tests if user posts record is deleted"""

        # post data to be deleted
        response = self.client.post("/api/v1/red-flags", json=self.data)
        self.assertEqual(response.status_code, 201)

        #delete posted data
        res = self.client.delete("/api/v1/red-flags/1")
        self.assertEqual(res.status_code, 200)

        # Test to see if it exists, should return a 404
        result = self.client.get('/api/v1/red-flags/1')
        self.assertEqual(result.status_code, 404)

    def test_if_id_non_existence_for_delete(self):
        """Test for when record does not exist for delete"""

        response = self.client.delete('/api/v1/red-flags/256')
        self.assertEquals(response.status_code,404)
        self.assertEquals(response.get_json(),{
            "message": "No record with this ID",
            "status": 404
                }
        )


    def test_it_edits_comment_option(self):
        """Test that it edits location of given id"""
    
        self.client.post('api/v1/red-flags', json=self.data)

        response = self.client.patch('api/v1/red-flags/1/comment', json={
            "comment": "police man taking bribe"
        })
        self.assertEqual(200, response.status_code)

    
    def test_it_does_not_edit_comment(self):
        """Tests it does not edit comment of an id that does not exist"""

        response = self.client.patch('api/v1/red-flags/440/comment', json={
            "comment": "paying to get served first"
        })
        self.assertEqual( response.get_json(),{"message": "No record with this ID",
                          "status": 404})

    def test_it_edits_location_option(self):
    
        self.client.post('api/v1/red-flags', json=self.data)

        response = self.client.patch('api/v1/red-flags/1/location', json={
            "location": "123, -0.2344"
        })
        self.assertEqual(200, response.status_code)

    
    def test_it_does_not_edit_location(self):
        """Tests that it does not edit location of an invalid id"""

        response = self.client.patch('api/v1/red-flags/334/location', json={
            "location": "1.333, 4.5566"
        })
        self.assertEqual( response.get_json(),{"message": "No record with this ID",
                          "status": 404})




if __name__ == '__main__':
    unittest.main()


