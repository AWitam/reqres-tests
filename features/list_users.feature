Feature: List users

  Scenario: Fetch a list of users
    Given I have a valid page number and per_page parameter
    When I fetch the list of users
    Then I should get a success list response
    And the list should contain users
