from datetime import datetime




def title():
    print("The Hotel Reservation Program")
    print()






def main():
    title()
    var = True
    while var:
        arrival_str = input("Enter arrival date (YYYY-MM-DD): ")
        departure_str = input("Enter departure date (YYYY-MM-DD): ")
        arrival_date = datetime.strptime(arrival_str,"%Y-%m-%d")
        if arrival_date.month == 8:
            price = float(105)
            msg = "(High Season)"
        else:
            price = float(85)
            msg = ""
        departure_date = datetime.strptime(departure_str, "%Y-%m-%d")
        date_format = "%B %d, %Y"
        total_nights = (departure_date - arrival_date).days
        total_rate = float(price * total_nights)
        print()
        print(f"Arrival date:   {arrival_date:{date_format}}")
        print(f"Departure date: {departure_date:{date_format}}")
        print(f"Nightly rate:   ${price:.2f}", msg)
        print(f"Total nights:   {total_nights}")
        print(f"Total rate:     ${total_rate:.2f}")
        print()

        again = input("Continue? (y/n): ")
        if again == "y":
            print()
            var = True
        else:
            var = False
    print()
    print("Bye!")


if __name__ == "__main__":
    main()