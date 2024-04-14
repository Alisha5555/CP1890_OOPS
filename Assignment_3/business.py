from database import TaskDB

class TaskManager:
    def __init__(self):
        self.db = TaskDB()

    def view_pending_tasks(self):
        """
        Fetches and displays all pending tasks.
        """
        pending_tasks = [task for task in self.db.get_all_tasks() if not task['completed']]
        if pending_tasks:
            for task in pending_tasks:
                print(f"{task['id']}. {task['description']}")
        else:
            print("No pending tasks.")

    def view_completed_tasks(self):
        """
        Fetches and displays all completed tasks.
        """
        completed_tasks = [task for task in self.db.get_all_tasks() if task['completed']]
        if completed_tasks:
            print("Completed Tasks:")
            for task in completed_tasks:
                print(f"{task['id']}. {task['description']} (DONE!)")
        else:
            print("No completed tasks.")

    def add_task(self):
        """
        Adds a new task.
        """
        task_description = input("Enter task description: ")
        self.db.add_task(task_description)
        print("Task added successfully.")

    def complete_task(self):
        """
        Marks a task as completed.
        """
        task_id = int(input("Number: "))
        if self.db.complete_task(task_id):
            print("Task marked as completed.")
        else:
            print("Task ID not found.")

    def delete_task(self):
        """
        Deletes a task.
        """
        task_id = int(input("Number: "))
        if self.db.delete_task(task_id):
            print("Task deleted successfully.")
        else:
            print("Task ID not found.")