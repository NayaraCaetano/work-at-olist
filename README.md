# Calls Bill Project

[![CircleCI](https://circleci.com/gh/NayaraCaetano/work-at-olist.svg?style=svg)](https://circleci.com/gh/NayaraCaetano/work-at-olist)

[![Maintainability](https://api.codeclimate.com/v1/badges/7bfc7b0f007441ac5a74/maintainability)](https://codeclimate.com/github/NayaraCaetano/work-at-olist/maintainability)

[![Test Coverage](https://api.codeclimate.com/v1/badges/7bfc7b0f007441ac5a74/test_coverage)](https://codeclimate.com/github/NayaraCaetano/work-at-olist/test_coverage)

Python application that receives call detail records
and calculates monthly bills for a given telephone number.


## Environment (main tools)

- Python 3.6.4
- Postgresql
- Django Rest Framework
- Celery
- SQS


## Deploy Structure

The application is ready to deploy on Heroku with the following details:
- Buildpacks
    - `heroku/python`
    - `https://github.com/heroku/heroku-buildpack-apt`
- Continuous integration and deployment: run tests in circleci and, if successful,
run deploy on Heroku.

Obs: Uses Honcho to run multiple processes (celery and gunicorn) in a single dyno.


## Quality tools

- Sentry is configured to report production errors
- CircleCI is configured to run tests and upload coverage in Codeclimate
- Codeclimate is configured to check code quality and show code coverage


## Api documentation

Provides a HTTP REST API with the following endpoints:


### Call Detail

Receives call details, saving on database.

- URL: `{base_url}/call/details
- HTTP request type: `POST`
- Authentication: None

- Params: This endpoint will accept two JSON templates:

1. Call Start Record

```
{
  "id":  // Record unique identificator;
  "type":  // Indicate if it's a call "start" or "end" record;
  "timestamp":  // The timestamp of when the event occured;
  "call_id":  // Unique for each call record pair;
  "source":  // The subscriber phone number that originated the call;
  "destination":  // The phone number receiving the call.
}
```

2. Call End Record

```
{
   "id":  // Record unique identificator;
   "type":  // Indicate if it's a call "start" or "end" record;
   "timestamp":  // The timestamp of when the event occured;
   "call_id":  // Unique for each call record pair.
}
```

Obs:
- If the record is sent more than once, the api will not save again on database
- If only one type of call was sent, api will consider the total cost as `None`


### Telephone bill

Returns the detailed bill of a telephone number.

- URL: `{base_url}/call/bill
- HTTP request type: `GET`
- Authentication: None
- Params:
    - `subscriber`: //required param
    - `period`: `month/year` // optional param
- Reponse format:

```
{
   "subscriber":  // The subscriber phone number that originated the call;
   "period":  // The period of the bill
   [
      {
        "destination": //The phone number receiving the call.
        "call_start_date":
        "call_start_time":
        "call_curation": //(hour, minute and seconds): e.g. 0h35m42s
        "call_price":  // e.g. R$ 3,96"
      }
      ...
   ]
}
```

Obs:
- If the period is not informed, the api will consider the last closed period
- It's only possible to get a telephone bill after the reference period has ended


## Quick start

1. **Database**

- Create a postgresql database with name `calls_bill`

2. **Requirements**

Apt-get requirements for celery with SQS:

- `libcurl4-gnutls-dev`
- `python3-dev`
- `python3-pycurl`

Pip requirements

- Install a python 3.6 virtualenv
- Execute: `pip install -r calls_bill_project/requirements/pip-dev.txt

3. Environment variables

Create a .env file containing:
```
AWS_ACCESS_KEY="{aws_access_key_for_sqs}"
AWS_SECRET_KEY="{aws_secret_key_for_sqs}"
```

4. **Migrate database**

- `python manage.py migrate`

5. **Initialize local server**

- `python manage.py runserver`

6. **Initialize celery worker**

- `celery -A calls_bill_project worker`

