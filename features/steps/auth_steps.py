from behave import given, when, then
import requests

BASE_URL = "http://127.0.0.1:8000"

@given('a user "{username}" exists with password "{password}"')
def step_register_user(context, username, password):
    requests.post(f"{BASE_URL}/register", json={
        "username": username,
        "password": password
    })

@when('she logs in with username "{username}" and password "{password}"')
def step_login(context, username, password):
    context.response = requests.post(f"{BASE_URL}/login", json={
        "username": username,
        "password": password
    })

@then("she should receive a valid token")
def step_check_token(context):
    assert context.response.status_code == 200
    assert "token" in context.response.json()

@then("she should receive a 401 status code")
def step_check_401(context):
    assert context.response.status_code == 401