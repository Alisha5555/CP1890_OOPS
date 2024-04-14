from dataclasses import dataclass
from datetime import datetime


# The Task class with Attributes task_name, task_description, due_date, and Method status
@dataclass
class Task:
    task_name: str
    task_description: str
    due_date: datetime

    def status(self):
        current_date = datetime.now()
        if self.due_date > current_date:
            return "Pending"
        else:
            return "Completed"


# The Homework(Task) class adding subject and task_status, also overriding status
@dataclass
class Homework(Task):
    subject: str
    task_status: str = "Not started"

    def status(self):
        if self.task_status == "Not started":
            return "Not started"
        elif self.task_status == "In progress":
            return "In progress"
        elif self.task_status == "Completed":
            return "Completed"
        else:
            return "Invalid task status"


# The Meeting(Task) class adding location and overriding the status
@dataclass
class Meeting(Task):
    location: str

    def status(self):
        current_date = datetime.now()
        if self.due_date > current_date:
            return "Scheduled"
        else:
            return "Happened"


# The main function to run the program
def main():
    homework = Homework("Math Homework", "Complete exercises 1-5", datetime(2023,
                                                                            10, 15), "Math")
    meeting = Meeting("Team Meeting", "Discuss project updates", datetime(2023,
                                                                          9, 20), "Office A")
    print("Homework:")
    print("Task Name:", homework.task_name)
    print("Task Description:", homework.task_description)
    print("Due Date:", homework.due_date)
    print("Subject:", homework.subject)
    print("Status:", homework.status())
    print("\n")
    print("Meeting:")
    print("Task Name:", meeting.task_name)
    print("Task Description:", meeting.task_description)
    print("Due Date:", meeting.due_date)
    print("Location:", meeting.location)
    print("Status:", meeting.status())


if __name__ == "__main__":
    main()
