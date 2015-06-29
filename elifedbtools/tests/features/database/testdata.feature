Feature: Test the test data
  In order to use the test data
  as a script 
  I will load the test data
  And I will see the test data

  Scenario: Load article test data
    Given I have the database <database>
    When I load the article test data
    Then I count the list total as <count>
    
  Examples:
    | database   | count
    | memdb      | 4
    
  Scenario: Load related article test data
    Given I have the database <database>
    When I load the related article test data
    Then I count the list total as <count>
    
  Examples:
    | database   | count
    | memdb      | 2
    
  Scenario: Count article records by doi
    Given I have the database <database>
    And I load the test data
    And I have the doi <doi>
    When I get article records by doi
    Then I count the list total as <count>
    
  Examples:
    | database   | doi                    | count
    | memdb      | a                      | 1
    | memdb      | b                      | 1
    | memdb      | x                      | 0
    
  Scenario: Count related article records by doi
    Given I have the database <database>
    And I load the test data
    And I have the doi <doi>
    When I get related article records by doi
    Then I count the list total as <count>
    
  Examples:
    | database   | doi                    | count
    | memdb      | a                      | 2
    | memdb      | b                      | 0

