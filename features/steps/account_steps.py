from behave import given, when, then
import requests

BASE_URL = "http://127.0.0.1:8000"

@given('a registered user "{username}" with password "{password}"')
def step_register_user(context, username, password):
    requests.post(f"{BASE_URL}/register", json={
        "username": username,
        "password": password
    })
    context.username = username

@given('he already has an account named "{account_name}"')
def step_existing_account(context, account_name):
    requests.post(f"{BASE_URL}/accounts/create", json={
        "username": context.username,
        "account_name": account_name
    })

@when('he creates a bank account named "{account_name}"')
def step_create_account(context, account_name):
    context.response = requests.post(f"{BASE_URL}/accounts/create", json={
        "username": context.username,
        "account_name": account_name
    })

@then('the account "{account_name}" should be created successfully')
def step_verify_account(context, account_name):
    assert context.response.status_code == 200
    assert account_name in context.response.json()["message"]

@then("he should receive a 400 status code")
def step_check_400(context):
    assert context.response.status_code == 400