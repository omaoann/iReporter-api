from datetime import datetime

users = []

class UserModel():

    def __init__(self):
        self.data = users


    def get_all_users(self):
        """This method fetches all users"""
        return self.data

    def get_single_user(self,email):
        """This method fetches a user by email"""

        user = [user for user in users
                   if user["email"] == email]
        return user


    def save(self,firstname,lastname,othername,email,phonenumber,username,password):
        """This method to create and saves a new user"""
        
        date = datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))
        details = {
            'id' : len(self.data)+1,
            'firstname' : firstname,
            'lastname' : lastname,
            'othername': othername,
            'email' : email,
            'phonenumber' : phonenumber,
            'username' : username,
            'password' : password,
            'registered': date,
            'isAdmin': False
        }
        self.data.append(details)
        return self.data
