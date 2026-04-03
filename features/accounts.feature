Feature: Create Bank Account
  As a registered user
  I want to create a bank account
  So that I can manage my money

  Scenario: Successfully create a new account
    Given a registered user "bob" with password "pass456"
    When he creates a bank account named "Savings"
    Then the account "Savings" should be created successfully

  Scenario: Cannot create duplicate account
    Given a registered user "charlie" with password "pass789"
    And he already has an account named "Checking"
    When he creates a bank account named "Checking"
    Then he should receive a 400 status code
