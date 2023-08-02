Feature: Dining Experience Manager

  Scenario: Display all meals with prices and topics
    Given the system has meals with prices and topics
      | Meal                    | Price | Topic          |
      | Pizza familiar          | 20    | Italian food   |
      | Hamburguesa doble       | 8.50  | American food  |
      | Ratatouille             | 40    | Especial food  |
      | Camarón al ajillo       | 35    | Especial food  |
    When the user displays the menu
    Then the output should contain all meals with prices and topics


  Scenario: Ensure meals are listed under correct topics
    Given the system has meals with topics
      | Meal                    | Topic          |
      | Pizza familiar          | Italian food   |
      | Hamburguesa doble       | American food  |
      | Ratatouille             | Especial food  |
      | Camarón al ajillo       | Especial food  |
    When the user displays the menu
    Then the output should list meals under their correct topics

  Scenario: Calculate total cost for a single meal
    Given the user selects a meal
      | Meal               | Quantity |
      | Pizza familiar     | 1        |
    When the system calculates the total cost
    Then the total cost should be 20


  Scenario: Calculate total cost for multiple meals
    Given the user selects multiple meals
      | Meal                    | Quantity |
      | Pizza familiar          | 1        |
      | Hamburguesa doble       | 2        |
      | Ratatouille             | 1        |
    When the system calculates the total cost
    Then the total cost should be 76


  Scenario: Display order summary for confirmation
    Given the user selects multiple meals
      | Meal                   | Quantity |
      | Pizza familiar         | 1        |
      | Hamburguesa doble      | 2        |
      | Ratatouille            | 1        |
    When the system generates the order summary
    Then the order summary should list all selected meals, their quantities, and the total cost
