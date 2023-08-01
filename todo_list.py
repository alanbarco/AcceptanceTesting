# todo_list.py
class Task:
    def __init__(self, name, status='Pending'):
        self.name = name
        self.status = status

    def mark_completed(self):
        self.status = 'Completed'

    def __str__(self):
        return f'{self.name} - {self.status}'


class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task_name):
        self.tasks.append(Task(task_name))

    def list_tasks(self):
        return [task.name for task in self.tasks]

    def mark_task_completed(self, task_name):
        for task in self.tasks:
            if task.name == task_name:
                task.mark_completed()
                break

    def clear_tasks(self):
        self.tasks = []


# main.py
if __name__ == "__main__":
    todo_list = TodoList()

    while True:
        print("1: Add task")
        print("2: List tasks")
        print("3: Mark task as complete")
        print("4: Clear all tasks")
        print("5: Exit")

        option = input("Choose an option: ")
        
        if option == "1":
            task_name = input("Enter task name: ")
            todo_list.add_task(task_name)

        elif option == "2":
            tasks = todo_list.list_tasks()
            for task in tasks:
                print(task)

        elif option == "3":
            task_name = input("Enter task name: ")
            todo_list.mark_task_completed(task_name)

        elif option == "4":
            todo_list.clear_tasks()

        elif option == "5":
            break

        else:
            print("Invalid option. Please try again.")
