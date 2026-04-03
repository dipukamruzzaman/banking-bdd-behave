Feature: User Authentication
  As a bank customer
  I want to log in securely
  So that I can access my account

  Scenario: Successful login with valid credentials
    Given a user "alice" exists with password "secret123"
    When she logs in with username "alice" and password "secret123"
    Then she should receive a valid token

  Scenario: Failed login with wrong password
    Given a user "alice" exists with password "secret123"
    When she logs in with username "alice" and password "wrongpass"
    Then she should receive a 401 status code