Feature: Todo List Management

  Scenario: Add a task to the to-do list
    Given the to-do list is empty
    When the user adds a task "Buy groceries" with priority "High"
    Then the to-do list should contain "Buy groceries" with priority "High"

  Scenario: List all tasks in the to-do list
    Given the to-do list contains tasks
      | Task          | Priority |
      | Buy groceries | High     |
      | Pay bills     | Low      |
    When the user lists all tasks
    Then the output should contain
      | Task          | Priority |
      | Buy groceries | High     |
      | Pay bills     | Low      |

  Scenario: Mark a task as completed
    Given the to-do list contains tasks
      | Task          | Priority | Status  |
      | Buy groceries | High     | Pending |
    When the user marks task "Buy groceries" as completed
    Then the to-do list should show task "Buy groceries" as completed

  Scenario: Delete a task from the to-do list
    Given the to-do list contains tasks
      | Task          | Priority |
      | Buy groceries | High     |
      | Pay bills     | Low      |
    When the user deletes task "Buy groceries"
    Then the to-do list should not contain "Buy groceries"

  Scenario: Edit the name of a task
    Given the to-do list contains tasks
      | Task          | Priority |
      | Buy groceries | High     |
      | Pay bills     | Low      |
    When the user edits the name of task "Buy groceries" to "Purchase groceries"
    Then the to-do list should contain "Purchase groceries" with priority "High"

  Scenario: Edit the priority of a task
    Given the to-do list contains tasks
      | Task          | Priority |
      | Buy groceries | High     |
      | Pay bills     | Low      |
    When the user edits the priority of task "Buy groceries" to "Low"
    Then the to-do list should contain "Buy groceries" with priority "Low"

  Scenario: Clear the entire to-do list
    Given the to-do list contains tasks
      | Task          | Priority |
      | Buy groceries | High     |
      | Pay bills     | Low      |
    When the user clears the to-do list
    Then the to-do list should be empty
