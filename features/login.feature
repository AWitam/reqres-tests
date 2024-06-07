Feature: User Login

  Scenario: Successfully login a user
    Given I have the following login data
      | email              | password |
      | eve.holt@reqres.in | pistol   |
    When I send a login request
    Then the response status should be 200
    And the login response should contain a token

  Scenario: Login with missing email
    Given I have the following login data
      | email | password |
      |       | passw0rd |
    When I send a login request
    Then the response status should be 400
    And the response should contain an error message

  Scenario: Login with missing password
    Given I have the following login data
      | email           | password |
      | user@example.com|          |
    When I send a login request
    Then the response status should be 400
    And the response should contain an error message