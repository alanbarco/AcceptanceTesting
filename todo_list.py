# todo_list.py
from datetime import date


class Task:
    def __init__(self, name, priority, status='Pending', date=date.today()):
        self.name = name
        self.priority = priority
        self.status = status
        self.date = date

    def mark_completed(self):
        self.status = 'Completed'

    def edit_name(self, name):
        self.name = name

    def edit_priority(self, priority):
        self.priority = priority

    def __str__(self):
        return f'{self.name} - {self.status} - {self.date} - {self.priority}'


class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task_name, task_priority):
        self.tasks.append(Task(task_name, task_priority))

    def list_tasks(self):
        i = 0
        print("#.TASKE NAME - STATUS - DATE - PRIORITY")
        for task in self.tasks:
            print(str(i)+"."+str(task))
            i = i+1

    def mark_task_completed(self, task_name):
        for task in self.tasks:
            if task.name == task_name:
                task.mark_completed()
                break

    def edit_task(self):
        print("1: Edit task name")
        print("2: Edit task priority")
        option = input("Choose an option: ")
        if option == "1":
            task_name = input("Enter task name: ")
            task.edit_name(task_name)
        elif option == "2":
            task_priority = input("Enter task priority: ")
            task.edit_priority(task_priority)
        else:
            print("Invalid option. Please try again.")

    def delete_task(self, task_number):
        del self.tasks[task_number]

    def clear_tasks(self):
        self.tasks = []


# main.py
if __name__ == "__main__":
    todo_list = TodoList()

    while True:
        print("\n1: Add task")
        print("2: List tasks")
        print("3: Mark task as complete")
        print("4: Clear all tasks")
        print("5: Delete task")
        print("6: Edit task")
        print("7: Exit")

        option = input("Choose an option: ")

        if option == "1":
            task_name = input("Enter task name: ")
            task_priority = input("Enter task priority: ")
            todo_list.add_task(task_name, task_priority)

        elif option == "2":
            todo_list.list_tasks()

        elif option == "3":
            task_name = input("Enter task name: ")
            todo_list.mark_task_completed(task_name)

        elif option == "4":
            todo_list.clear_tasks()

        elif option == "5":
            todo_list.list_tasks()
            task_number = int(input("Enter task number to delete: "))
            todo_list.delete_task(task_number)
        elif option == "6":
            todo_list.list_tasks()
            task_number = int(input("Enter task number to edit: "))
            task = todo_list.tasks[task_number]
            todo_list.edit_task()

        elif option == "7":
            break

        else:
            print("Invalid option. Please try again.")
