Feature: User Registration

  Scenario: Successfully register a new user
    Given I have the following user data
      | email              | password |
      | eve.holt@reqres.in | pistol   |
    When I send a registration request
    Then the response status should be 200
    And the response should contain a token

  Scenario: Register with missing email
    Given I have the following user data
      | email | password |
      |       | passw0rd |
    When I send a registration request
    Then the response status should be 400
    And the response should contain an error message


  Scenario: Register with missing password
    Given I have the following user data
      | username | email           | password |
      | user123  | user@example.com|          |
    When I send a registration request
    Then the response status should be 400
    And the response should contain an error message