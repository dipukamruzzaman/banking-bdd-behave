Feature: Deposit and Withdrawal
  As a bank customer
  I want to deposit and withdraw money
  So that I can manage my balance

  Scenario: Successfully deposit money
    Given an account "savings001" with balance 0
    When she deposits 500 into "savings001"
    Then the balance of "savings001" should be 500

  Scenario: Successfully withdraw money
    Given an account "savings002" with balance 1000
    When she withdraws 200 from "savings002"
    Then the balance of "savings002" should be 800

  Scenario: Cannot withdraw more than balance
    Given an account "savings003" with balance 100
    When she withdraws 500 from "savings003"
    Then she should receive an insufficient funds error
