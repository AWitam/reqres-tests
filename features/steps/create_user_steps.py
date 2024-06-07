import requests
from behave import given, when, then

USERS_API_URL = "https://reqres.in/api/users"

@given('I have the user details')
def step_given_user_details(context):
   for row in context.table:
        context.user_data = { "first_name": row['first_name'], "job": row['job']} 

@when('I create a new user')
def step_create_user(context):
    response = requests.post(USERS_API_URL, json=context.user_data)
    context.response = response
    context.user_id = response.json().get('id')

@then('I should get a success response')
def step_verify_success_response(context):
    assert context.response.status_code == 201
    assert 'first_name' in context.response.json()
    assert 'job' in context.response.json()

@then('the user should exist in the system') #expected to fail as reqres.in does not store data
def step_verify_user_exists(context):
    user_id = context.user_id
    response = requests.get(f"{USERS_API_URL}/{user_id}")
    assert response.status_code == 200 
    user_data = response.json().get('data')
    assert user_data['first_name'] == context.user_data['first_name']  
    assert user_data['job'] == context.user_data['job']
