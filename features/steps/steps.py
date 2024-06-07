import requests
from behave import *
import json

API_URL = 'https://reqres.in/api/register'
headers = {
  'Content-Type': 'application/json'
}

@given('I have the following user data')
def step_given_i_have_user_data(context):
    for row in context.table:
        context.user_data = { "email": row['email'], "password": row['password']} 
        
        
@when('I send a registration request')
def step_when_send_registration_request(context):
    print(context.user_data)
    user_data = json.dumps(context.user_data)
    context.response = requests.request("POST", API_URL, headers=headers, data=user_data)
    
@then('the response status should be {expected_status:d}')
def step_then_response_status_should_be(context, expected_status):
    print(context.response.status_code)
    assert context.response.status_code == expected_status

@then('the response should contain a token')
def step_then_response_should_contain_token(context):
    data = context.response.json()
    assert 'token' in data

@then('the response should contain an error message')
def step_then_response_should_contain_error_message(context):
    data = context.response.json()
    assert 'error' in data