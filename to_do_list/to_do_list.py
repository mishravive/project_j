tasks = []

def add_task(task):
    tasks.append(task)
    print("Task added:", task)


def view_tasks():
    if tasks:
        print("Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    else:
        print("No tasks to display.")

def complete_task(task_index):
    if 1 <= task_index <= len(tasks):
        completed_task = tasks.pop(task_index - 1)
        print("Task completed:", completed_task)
    else:
        print("Invalid task index.")

while True:
    print("\nSelect an option:")
    print("1. Add task")
    print("2. View tasks")
    print("3. Complete task")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        new_task = input("Enter the task: ")
        add_task(new_task)
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        task_index = int(input("Enter the task number to mark as complete: "))
        complete_task(task_index)
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please choose again.")