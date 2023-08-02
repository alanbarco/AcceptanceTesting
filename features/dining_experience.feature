Feature: Dining Experience Manager

    Scenario: User enters a valid quantity
        Given the system has a meal "Pizza familiar"
        When the user enters a quantity "2" for the meal
        Then the system should accept the quantity

    Scenario: User enters zero quantity
        Given the system has a meal "Pizza familiar"
        When the user enters a quantity "0" for the meal
        Then the system should not accept the quantity and display an error message

    Scenario: User enters a negative quantity
        Given the system has a meal "Pizza familiar"
        When the user enters a quantity "-1" for the meal
        Then the system should not accept the quantity and display an error message
    Scenario: User orders more than 5 meals
        Given the system has a meal "Pizza familiar"
        When the user orders a total quantity of "6" meals
        Then the system should apply a "10" percent discount to the total cost