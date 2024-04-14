from dataclasses import dataclass
from datetime import datetime


# The Event class with attributes name, location, start_date, end_date and method duration
@dataclass
class Event:
    name: str = ''
    location: str = ''
    start_date: datetime = None
    end_date: datetime = None

    def duration(self):
        return (self.end_date - self.start_date).days


# The Conference(Event) class adding attendees and overriding duration
@dataclass
class Conference(Event):
    attendees: int = 0

    def duration(self):
        return (self.end_date - self.start_date).days * 24


# The main function to run the program
def main():
    event = Event("Birthday Party", "New York", datetime(2023, 8, 25),
                  datetime(2023, 8, 26))

    conference = Conference("Tech Conference", "San Francisco", datetime(2023, 9, 15), datetime(2023, 9, 17), 500)
    print("Event:")
    print("Name:", event.name)
    print("Location:", event.location)
    print("Start Date:", event.start_date)
    print("End Date:", event.end_date)
    print("Duration (days):", event.duration())
    print("\n")
    print("Conference:")
    print("Name:", conference.name)
    print("Location:", conference.location)
    print("Start Date:", conference.start_date)
    print("End Date:", conference.end_date)
    print("Attendees:", conference.attendees)
    print("Duration (hours):", conference.duration())


if __name__ == "__main__":
    main()
