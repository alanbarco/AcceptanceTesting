from datetime import date
options = ["Add a new task","List all the tasks", "Mark a task as completed",
 "Clear the entire to-do list", "Delete a task", "Edit a task", "Exit"]
tasks_name = []
tasks_prior = []
tasks_state = []
tasks_date = []

def print_menu():
    i = 0
    for option in options:
        i = i+1
        print(i,option)

def validate_option(i_option):
    if(i_option > len(options) or i_option < 0):
        raise ValueError("ERROR: The option is incorrect")

def add_task():
    str_task = input("Write the new task(Name, Priority): ")
    task = str_task.split(",")
    tasks_name.append(task[0])
    tasks_prior.append(task[1])
    tasks_state.append("Pending")
    tasks_date.append(date.today())
    print("Task added correctly!")

def list_tasks():
    print("#\t | NAME\t | PRIORITY\t | STATE| DATE")
    for i in range(len(tasks_name)):
        print(i,"\t",tasks_name[i],"\t",tasks_prior[i],"\t", tasks_state[i], tasks_date[i])

def complete_task():
    list_tasks()
    i_task = int(input("Select the task you want to complete: "))
    tasks_state[i_task] = "Completed"
    print("Task marked as completed!")
    
def clear_all_tasks():
    tasks_name.clear()
    tasks_prior.clear()
    tasks_state.clear()
    tasks_date.clear()
    print("Task list cleared!")

def delete_task():
    list_tasks()
    i_task = int(input("Select the task you want to delete: "))
    del tasks_name[i_task]
    del tasks_prior[i_task]
    del tasks_state[i_task]
    del tasks_date[i_task]
    print("Task deleted!")

if __name__ == '__main__':
    i_option = 0
    cases = {1: add_task, 2: list_tasks, 3: complete_task, 4: clear_all_tasks, 5: delete_task}
    while i_option != 7:
        print("\n******TO DO LIST MANAGER******")
        print_menu()
        while True:
            try:
                i_option = int(input("Select a option:"))
                validate_option(i_option)
            except ValueError as e:
                print(e)
            else:
                break
        function = cases.get(i_option)
        function()
        