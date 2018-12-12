####Registration data####
registration_data = {
        'firstname': 'Jane',
        'othername': 'doe',
        'lastname': 'jose',
        'username': 'janedoe',
        'email': 'janedoe@gmail.com',
        'phonenumber': '0711122334',
        'password': '12345'
        }
registration_data_1 = {
        'firstname': 'ann',
        'othername': 'kerubo',
        'lastname': 'omao',
        'username': 'annkay',
        'email': 'annkay@gmail.com',
        'phonenumber': '0711122300',
        'password': '456789'
        }
empty_reg_data = {
        'firstname': '',
        'othername': 'doe',
        'lastname': 'jose',
        'username': '',
        'email': 'janedoe@gmail.com',
        'phonenumber': '0711122334',
        'password': '12345'
        }
reg_invalid_email = {
        'firstname': 'jane',
        'othername': 'doe',
        'lastname': 'jose',
        'username': 'janedoe',
        'email': 'janedoe@gmail',
        'phonenumber': '0711122334',
        'password': '12345'
        }
####login details####
data_login = {
        'email': 'janedoe@gmail.com',
        'password': '12345'
        }
data_login_1 = {
        'email': 'annkay@gmail.com',
        'password': '456789'
        }
admin_login = {
        'email':'admin@gmail.com',
        'password':'adminstrator'
}
login_empty_field = {
        'email': '',
        'password': '12345'
        }
login_invalid_name = {
        'email': 'mototo@gmail.com',
        'password': '12345'
        }
invalid_password = {
    'email': 'janedoe@gmail.com',
    'password' : 'qwerty'
}
login_invalid_email = {
    'email': 'janedoecom',
    'password' : '12345'    
}

####incidents data####
record_data= {
        'flag_type': 'Intervention',
        'location': '-1.223,1.2333',
        'comment': 'Police officer taking bribes'
        }

reccord_empty_field= {
        'flag_type': 'Intervention',
        'location': '',
        'comment': 'Police officer taking bribes'
        }

reccord_wrong_location= {
        'flag_type': 'Intervention',
        'location': '1010,23039',
        'comment': 'Police officer taking bribes'
        }

comment= {
        'comment': 'Roads not good for transportation'
        }
empty_comment= {
        'comment': ''
        }

location= {
        'location': '-11111,1.11111'
        }
empty_location= {
        'location': ''
        }
status = {
        'status':'Under Investigation'
}
empty_status = {
        'status':''
}

