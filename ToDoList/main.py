from task_manager import *

while True:
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task Completed")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        task = input("Enter task: ")
        add_task(task)
        print("Task Added!")

    elif choice == "2":
        tasks = view_tasks()

        if not tasks:
            print("No tasks found.")
        else:
            for i, task in enumerate(tasks):
                print(f"{i+1}. {task['task']} [{task['status']}]")

    elif choice == "3":
        task_num = int(input("Enter task number: "))
        mark_completed(task_num - 1)
        print("Task Completed!")

    elif choice == "4":
        task_num = int(input("Enter task number: "))
        delete_task(task_num - 1)
        print("Task Deleted!")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid Choice")