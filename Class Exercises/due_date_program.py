from datetime import datetime
def title():
    print("The Invoice Due Date Program")

def main():
    date = input("Enter the invoice date (MM/DD/YY): ")
    date = datetime.strptime(date, "%m/%d/%Y")
    print(date.strftime("%B %d, %Y"))
    due = "2/13/2021"
    due_date = datetime.strptime(due, "%m/%d/%Y")
    print(due_date)
main()