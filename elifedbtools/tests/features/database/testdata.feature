Feature: Test the test data
  In order to use the test data
  as a script 
  I will load the test data
  And I will see the test data

  Scenario: Load article test data
    Given I load the article test data
    When I count the list total as <count>
    
  Examples:
    | count
    | 4
    
  Scenario: Load related article test data
    Given I load the related article test data
    When I count the list total as <count>
    
  Examples:
    | count
    | 2
    
  Scenario: Count article records by doi
    Given I load the test data
    And I have the doi <doi>
    When I get article records by doi
    Then I count the list total as <count>
    
  Examples:
    | doi                    | count
    | a                      | 1
    | b                      | 1
    | x                      | 0
    
  Scenario: Count related article records by doi
    Given I load the test data
    And I have the doi <doi>
    When I get related article records by doi
    Then I count the list total as <count>
    
  Examples:
    | doi                    | count
    | a                      | 2
    | b                      | 0

