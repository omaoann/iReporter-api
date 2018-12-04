# iReporter-api

[![Build Status](https://travis-ci.org/omaoann/iReporter-api.svg?branch=ch-intergrate-travis-CI-162337060)](https://travis-ci.org/omaoann/iReporter-api)
[![Coverage Status](https://coveralls.io/repos/github/omaoann/iReporter-api/badge.svg?branch=ch-intergrate-travis-CI-162337060)](https://coveralls.io/github/omaoann/iReporter-api?branch=ch-intergrate-travis-CI-162337060)

iReporter is an application that enables any/every citizen to bring any form of corruption to the notice of appropriate authorities and the general public. Users can also report on things that needs government intervention

### Features Endpoints:

| Method | Route | Endpoint Functionality |
| :---         |     :---       |          :--- |
| POST   | /api/v1/signup     | Creates a user account    |
| GET     | /api/v1/red-flags        | Gets all red-flag records     |
| GET     | /api/v1/red-flags/id      |Gets a single red flag record     |
| POST     | /api/v1/red-flags       | Add a new red flag record     |
| PATCH     | /api/v1/red-flags/id/location        | Enable user to edit their loction      |
| PATCH     | /api/v1/red-flags/id/comment       | Enable user to edit their comment     |
| DELETE     | /api/v1/red-flags/id       | Enable user to delete a specific red flag record     |    |

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

http://127.0.0.1:5000/api/v1/signup

Key:content-type value:Application Json

Enter the following data in the body section

          {  "firstname" : "Ann",
            "lastname" : "omao",
            "othername" : "kerubo",
            "email" : "annkay2303@gmail.com",
            "phonenumber" : "0712345678",
            "username" : "annkay",
            "password" : "123456"  }

The expected outcome should be:
{
                "status": 201,
                "data": [
                    {
                        "id": 1,
                        "message": "A new user has been created"
                     }
                ]
            }


Create new redflag record

http://127.0.0.1:5000/api/v1/red-flags

Key:content-type value:Application Json

Enter the following data in the body section
        
          {  "createdBy" : "23",
            "type" : "red-flag",
            "location" : "123,345",
            "comment" : "bribe taken" }
                
The expected outcome should be:

{
                "status": 201,
                "data": [
                    {
                        "id": 1,
                        "message": "created red-flag record"
                     }
                ]
            }
