from behave import given, when, then
from todo_list import TodoList

@given('the to-do list is empty')
def step_given_empty_todo_list(context):
    context.todo_list = TodoList()

@when('the user adds a task "{task_name}"')
def step_when_user_adds_task(context, task_name):
    context.todo_list.add_task(task_name)

@then('the to-do list should contain "{task_name}"')
def step_then_todo_list_contains(context, task_name):
    assert task_name in context.todo_list.list_tasks()

@given('the to-do list contains tasks')
def step_given_todo_list_with_tasks(context):
    context.todo_list = TodoList()
    for row in context.table:
        context.todo_list.add_task(row['Task'])

@when('the user lists all tasks')
def step_when_user_lists_all_tasks(context):
    context.listed_tasks = context.todo_list.list_tasks()

@then('the output should contain')
def step_then_output_should_contain(context):
    for row in context.table:
        assert row['Task'] in context.listed_tasks

@when('the user marks task "{task_name}" as completed')
def step_when_user_marks_task_as_completed(context, task_name):
    context.todo_list.mark_task_completed(task_name)

@then('the to-do list should show task "{task_name}" as completed')
def step_then_todo_list_should_show_task_as_completed(context, task_name):
    task = next((task for task in context.todo_list.tasks if task.name == task_name), None)
    assert task is not None
    assert task.status == 'Completed'

@when('the user clears the to-do list')
def step_when_user_clears_todo_list(context):
    context.todo_list.clear_tasks()

@then('the to-do list should be empty')
def step_then_todo_list_should_be_empty(context):
    assert not context.todo_list.list_tasks()
