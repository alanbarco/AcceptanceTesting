from behave import given, when, then
from todo_list import TodoList, Task


@given('the to-do list is empty')
def step_given_empty_todo_list(context):
    context.todo_list = TodoList()


@when('the user adds a task "{task_name}" with priority "{priority}"')
def step_when_user_adds_task(context, task_name, priority):
    context.todo_list.add_task(task_name, priority)


@then('the to-do list should contain "{task_name}" with priority "{priority}"')
def step_then_todo_list_contains(context, task_name, priority):
    tasks = [str(task) for task in context.todo_list.tasks if task.name ==
             task_name and task.priority == priority]
    assert tasks


@given('the to-do list contains tasks')
def step_given_todo_list_with_tasks(context):
    context.todo_list = TodoList()
    for row in context.table:
        context.todo_list.add_task(row['Task'], row['Priority'])


@when('the user lists all tasks')
def step_when_user_lists_all_tasks(context):
    context.listed_tasks = context.todo_list.list_tasks()


@then('the output should contain')
def step_then_output_should_contain(context):
    for row in context.table:
        tasks = [str(task) for task in context.todo_list.tasks if task.name ==
                 row['Task'] and task.priority == row['Priority']]
        assert tasks


@when('the user marks task "{task_name}" as completed')
def step_when_user_marks_task_as_completed(context, task_name):
    context.todo_list.mark_task_completed(task_name)


@then('the to-do list should show task "{task_name}" as completed')
def step_then_todo_list_should_show_task_as_completed(context, task_name):
    tasks = [str(task) for task in context.todo_list.tasks if task.name ==
             task_name and task.status == 'Completed']
    assert tasks


@when('the user deletes task "{task_name}"')
def step_when_user_deletes_task(context, task_name):
    task_index = next((index for index, task in enumerate(
        context.todo_list.tasks) if task.name == task_name), None)
    if task_index is not None:
        context.todo_list.delete_task(task_index)


@then('the to-do list should not contain "{task_name}"')
def step_then_todo_list_does_not_contain(context, task_name):
    tasks = [str(task)
             for task in context.todo_list.tasks if task.name == task_name]
    assert not tasks


@when('the user edits the name of task "{task_name}" to "{new_task_name}"')
def step_when_user_edits_task_name(context, task_name, new_task_name):
    task = next(
        (task for task in context.todo_list.tasks if task.name == task_name), None)
    if task:
        task.edit_name(new_task_name)


@when('the user edits the priority of task "{task_name}" to "{new_priority}"')
def step_when_user_edits_task_priority(context, task_name, new_priority):
    task = next(
        (task for task in context.todo_list.tasks if task.name == task_name), None)
    if task:
        task.edit_priority(new_priority)


@when('the user clears the to-do list')
def step_when_user_clears_todo_list(context):
    context.todo_list.clear_tasks()


@then('the to-do list should be empty')
def step_then_todo_list_is_empty(context):
    assert not context.todo_list.tasks
