Feature: Test the test data
  In order to use the test data
  as a script 
  I will load the test data
  And I will see the test data

  Scenario: Load article test data
    Given I load the article test data
    When I count the list items
    Then I count the total as <count>
    
  Examples:
    | count
    | 4
    
  Scenario: Load related article test data
    Given I load the related article test data
    When I count the list items
    Then I count the total as <count>
    
  Examples:
    | count
    | 2