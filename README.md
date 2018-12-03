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