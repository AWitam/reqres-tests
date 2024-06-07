import requests
from behave import given, when, then

LOGIN_API_URL = 'https://reqres.in/api/login'

@given('I have the following login data')
def step_given_login_data(context):
    context.user_data = {}
    for row in context.table:
        context.user_data['email'] = row.get('email')
        context.user_data['password'] = row.get('password')

@when('I send a login request')
def step_when_send_login_request(context):
    login_data = context.user_data
    response = requests.post(LOGIN_API_URL, json=login_data)
    context.response = response

@then('the response status should be {expected_status:d}')
def step_then_response_status_should_be(context, expected_status):
    assert context.response.status_code == expected_status, \
        f"Expected status {expected_status}, but got {context.response.status_code}"

@then('the login response should contain a token')
def step_then_response_should_contain_token(context):
    data = context.response.json()
    assert 'token' in data, "Token not found in response"

@then('the login response should contain an error message')
def step_then_response_should_contain_error_message(context):
    data = context.response.json()
    assert 'error' in data, "Error message not found in response"