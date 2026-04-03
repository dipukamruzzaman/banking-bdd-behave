from behave import given, when, then
import requests

BASE_URL = "http://127.0.0.1:8000"

@given('an account "{account}" with balance {balance:d}')
def step_init_account(context, account, balance):
    requests.post(f"{BASE_URL}/accounts/init", json={
        "account": account,
        "amount": balance
    })
    context.account = account

@when('she deposits {amount:d} into "{account}"')
def step_deposit(context, amount, account):
    context.response = requests.post(f"{BASE_URL}/deposit", json={
        "account": account,
        "amount": amount
    })

@when('she withdraws {amount:d} from "{account}"')
def step_withdraw(context, amount, account):
    context.response = requests.post(f"{BASE_URL}/withdraw", json={
        "account": account,
        "amount": amount
    })

@then('the balance of "{account}" should be {expected:d}')
def step_check_balance(context, account, expected):
    assert context.response.status_code == 200
    assert context.response.json()["balance"] == expected

@then("she should receive an insufficient funds error")
def step_insufficient_funds(context):
    assert context.response.status_code == 400
    assert context.response.json()["detail"] == "Insufficient funds"