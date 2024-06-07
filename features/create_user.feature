Feature: Create user

  Scenario: Create a user and verify the user exists
    Given I have the user details
      | first_name | job      |
      | Jogn | magician |
    When I create a new user
    Then I should get a success response
    And the user should exist in the system
