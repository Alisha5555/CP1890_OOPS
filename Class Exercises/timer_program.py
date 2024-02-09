from datetime import datetime, time

def main():
    print("The Timer Program\n")

    input("Press Enter to start...")
    start_time = datetime.now()
    print("Start time:", start_time)
    print()

    input("Press Enter to stop...")
    stop_time = datetime.now()
    print("Stop time:", stop_time)
    print()

    elapsed_time = stop_time - start_time
    days = elapsed_time.days
    minutes = elapsed_time.seconds // 60
    seconds = elapsed_time.seconds % 60
    microseconds = elapsed_time.microseconds

    hours = minutes // 60
    minutes = seconds % 60

    time_object = time(hours, minutes, seconds, microseconds)

    print("Elapsed time")
    if days > 0:
        print("Days: ",days)
    print("Time: ", time_object)


main()