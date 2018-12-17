# iReporter-api

[![Build Status](https://travis-ci.org/omaoann/iReporter-api.svg?branch=develop)](https://travis-ci.org/omaoann/iReporter-api)
[![Coverage Status](https://coveralls.io/repos/github/omaoann/iReporter-api/badge.svg?branch=develop)](https://coveralls.io/github/omaoann/iReporter-api?branch=develop)
[![Maintainability](https://api.codeclimate.com/v1/badges/b6e2fd0b59d4f4c0316e/maintainability)](https://codeclimate.com/github/omaoann/iReporter-api/maintainability)

iReporter is an application that enables any/every citizen to bring any form of corruption to the notice of appropriate authorities and the general public. Users can also report on things that needs government intervention

### Features v1 Endpoints:

| Method | Route | Endpoint Functionality |
| :---         |     :---       |          :--- |
| POST   | /api/v1/signup     | Creates a user account    |
| GET     | /api/v1/red-flags        | Gets all red-flag records     |
| GET     | /api/v1/red-flags/id      |Gets a single red flag record     |
| POST     | /api/v1/red-flags       | Add a new red flag record     |
| PATCH     | /api/v1/red-flags/id/location        | Enable user to edit their loction      |
| PATCH     | /api/v1/red-flags/id/comment       | Enable user to edit their comment     |
| DELETE     | /api/v1/red-flags/id       | Enable user to delete a specific red flag record     |    |

### Features v2 Endpoints:

| Method | Route | Endpoint Functionality |
| :---         |     :---       |          :--- |
| POST   | /api/v2/auth/signup     | Creates a user account    |
| POST   | /api/v2/auth/login     | Logs in a user into their account    |
| POST     | /api/v2/interventions       | Add a new incident record     |
| GET     | /api/v2/intervention        | Gets all intervention records     |
| GET     | /api/v2/intervention/id      |Gets a single intervention record     |
| PATCH     | /api/v2/intervention/id/location        | Enable user to edit their loction      |
| PATCH     | /api/v2/intervention/id/comment       | Enable user to edit their comment     |
| DELETE     | /api/v2/intervention/id       | Enable user to delete an intervention record     |    |
| GET     | /api/v2/red-flag        | Gets all red-flag records     |
| GET     | /api/v2/red-flag/id      |Gets a single red flag record     |
| PATCH     | /api/v2/red-flag/id/location        | Enable user to edit their loction      |
| PATCH     | /api/v2/red-flag/id/comment       | Enable user to edit their comment     |
| DELETE     | /api/v2/red-flag/id       | Enable user to delete a specific red flag record     |    |
| PATCH    | /api/v2/red-flag/id/status       | Enable admin to edit status of a redflag     |    |
| PATCH    | /api/v2/intervention/id/status       | Enable admin to edit status of an intervention     |    |

### Installation Procedure

clone the repo

``` 
git clone https://github.com/omaoann/iReporter-api.git

```

create and activate the virtual environment

```
virtualenv <environment name>

```
```
$source <env name>/bin/activate (in bash)

```
install project dependencies:

```
$pip install -r requirements.txt

```
### Running

Running the application
```
python run.py

```
Test the endpoints using Postman http://127.0.0.1:5000/


### Sample Tests

```
User Registration Endpoint

http://127.0.0.1:5000/api/v2/auth/signup

Key:content-type value:Application Json

Enter the following data in the body section

          {  "firstname" : "Ann",
            "lastname" : "omao",
            "othername" : "kerubo",
            "email" : "annkay2303@gmail.com",
            "phonenumber" : "0712345678",
            "username" : "annkay",
            "password" : "123456"  }

User login Endpoint

http://127.0.0.1:5000/api/v2/auth/login

Key:content-type value:Application Json

Enter the following data in the body section

          { 
            "email" : "annkay2303@gmail.com",
            "password" : "123456"  }


Create new incident record

http://127.0.0.1:5000/api/v2/red-flag

Key:content-type value:Application Json

Enter the following data in the body section
        
          { 
            "type" : "red-flag",
            "location" : "-1.23,3.45",
            "comment" : "bribe taken" }
                

