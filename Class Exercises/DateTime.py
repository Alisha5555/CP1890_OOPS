from datetime import datetime, timedelta

def get_invoice_date():
    invoice_date_str = input("Enter the invoice date (MM/DD/YY) : ")
    invoice_date = datetime.strptime(invoice_date_str, "%m/%d/%y")
    return invoice_date

def main():
    print("The Invoice Due Date program\n")

    do_again = 'y'
    while do_again.lower() == 'y':
        invoice_date = get_invoice_date()
        print()

        #calculations
        due_date = invoice_date + timedelta(days=30)
        current_date = datetime.now()
        days_overdue = (current_date - due_date).days

        #the display stuff
        date_format = "%B %d, %Y"
        print(f"Invoice Date:       {invoice_date:{date_format}}")
        print(f"Due Date:           {due_date:{date_format}}")
        print(f"Current Due Date:   {current_date:{date_format}}")

        #Update the choice
        if  days_overdue > 0:
            print(f"This invoice is {days_overdue} day(s) overdue.")
        else:
            days_due = days_overdue * -1
            print(f"This invoice is due in {days_due} day(s)")
        print()
        do_again = input("Continue? (y/n): ")
        print()

    print("Thank you for using this program.")


if __name__ == '__main__':
    main()