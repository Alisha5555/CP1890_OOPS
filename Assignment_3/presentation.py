from Assignment_3.business import TaskManager

def display_tasks():
    print("Task List")
    print("COMMAND MENU")
    print("view \t- View pending tasks")
    print("history - View completed tasks")
    print("add \t- Add a task")
    print("complete - Complete a task")
    print("delete \t- Delete a task")
    print("exit \t- Exit program")


def main(task_manager):
    while True:
        command = input("\nCommand: ").strip().lower()

        if command == 'view':
            task_manager.view_pending_tasks()
        elif command == 'history':
            task_manager.view_completed_tasks()
        elif command == 'add':
            task_manager.add_task()
        elif command == 'complete':
            task_manager.complete_task()
        elif command == 'delete':
            task_manager.delete_task()
        elif command == 'exit':
            print("Exiting program...")
            break
        else:
            print("Invalid command. Please enter a valid command.")

if __name__ == "__main__":
    task_manager = TaskManager()

    while True:
        display_tasks()
        main(task_manager)