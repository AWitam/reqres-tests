import requests
from behave import given, when, then

USERS_API_URL = "https://reqres.in/api/users"

@given('I have a valid page number and per_page parameter')
def step_given_valid_page_parameters(context):
    context.page = 2
    context.per_page = 5

@when('I fetch the list of users')
def step_fetch_list_of_users(context):
    response = requests.get(USERS_API_URL, params={"page": context.page, "per_page": context.per_page})
    context.response = response
    context.users = response.json().get('data')

@then('I should get a success list response')
def step_verify_success_response(context):
    assert context.response.status_code == 200

@then('the list should contain users')
def step_verify_list_contains_users(context):
    assert isinstance(context.users, list)
    assert len(context.users) == context.per_page

    first_user = context.users[0]
    assert 'id' in first_user
    assert 'email' in first_user
    assert 'first_name' in first_user
    assert 'last_name' in first_user
    assert 'avatar' in first_user
