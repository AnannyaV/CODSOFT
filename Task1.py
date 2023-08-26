# COMMAND-LINE TO-DO LIST USING PYTHON #

# create a to-do list
todo_list = []

# function to add a task to the list
def add_task():
    task = input("Enter a task: ")
    todo_list.append(task)
    print("Task added successfully!")


# function to update a task in the list
def update_task():
    task_index = int(input("Enter the index of the task to update: "))
    task = input("Enter the new task: ")
    todo_list[task_index] = task
    print("Task updated successfully!")


# function to delete a task from the list
def delete_task():
    task_index = int(input("Enter the index of the task to delete: "))
    del todo_list[task_index]
    print("Task deleted successfully!")


# function to display the to-do list
def display_list():
    print("To-do list:")
    for i, task in enumerate(todo_list):
        print(f"{i+1}. {task}")
    print('\n')
    print("-------------------------------")

# main function to run the program
def main():
    while True:
        print("1. Add task")
        print("2. Update task")
        print("3. Delete task")
        print("4. Display to-do list")
        print("5. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_task()
        elif choice == 2:
            update_task()
        elif choice == 3:
            delete_task()
        elif choice == 4:
            display_list()
        elif choice == 5:
            break
        else:
            print("Invalid choice!")


# run the program
if __name__ == "__main__":
    main()