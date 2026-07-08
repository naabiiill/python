#list

task_list = []

"""

1.view all tasks
2.add new task
3.shift a new task above a specific task
4.remove a task
5. backup task
6. clear all task

"""
#for and while loop

while True:
    print("\n----- Task Manager -----")
    print("1. View all tasks")
    print("2. Add new task")
    print("3. Shift a new task above a specific task")
    print("4. Remove a task")
    print("5. Backup tasks")
    print("6. Clear all tasks")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    if choice == '1':
        if len(task_list) == 0:
            print("No tasks available.")
        else:
            print("\n----- Task List -----")
            for task in task_list:
                print(task)

    elif choice == '2':
        new_task = input("Enter the new task: ")
        task_list.append(new_task)
        print(f"Task '{new_task}' added successfully.")

    elif choice == '3':
        new_special_task = input("Enter the new task to shift: ")
        index_of_task = int (input("enter the index of the task to shift: "))  

        if len(task_list) == 0 and len(task_list) < index_of_task:
            task_list.append(new_special_task)
            print ("new task added successfully")
        else: 
            task_list.insert(index_of_task, new_special_task)
            print("Task shifted successfully.")

    elif choice == '4':
        if len(task_list) == 0:
            print("No tasks available to remove.")
        else:
            task_to_remove = input("Enter the task to remove: ")

            if task_to_remove in task_list:
                task_list.remove(task_to_remove)
                print("task is removed successfully")
            else:
                print("Task not found in the list.")
    elif choice == '5': 
        backup_task_list = task_list.copy()
        print("Tasks backed up successfully.")
    elif choice == '6':    

        task_list.clear()
        print("All tasks cleared successfully.")
    elif choice == '7':
        print("Exiting the Task Manager.")
        break