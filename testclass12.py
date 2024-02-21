from test12 import Countdown
from datetime import datetime
def main():
    now = datetime.now()

    target_datetime1_str = input("Datetime1 format(year,month,day,hour,minute): ")
    target_datetime1 = datetime.strptime(target_datetime1_str, "%Y,%m,%d,%H,%M")
    countdown1 = Countdown(target_datetime1)
    target_datetime2_str = input("Datetime2 format(year,month,day,hour,minute): ")
    target_datetime2 = datetime.strptime(target_datetime2_str, "%Y,%m,%d,%H,%M")
    countdown2 = Countdown(target_datetime2)
    target_datetime3_str = input("Datetime3 format(year,month,day,hour,minute): ")
    target_datetime3 = datetime.strptime(target_datetime3_str, "%Y,%m,%d,%H,%M")
    countdown3 = Countdown(target_datetime3)
    print()
    print(countdown1.time_left())
    print(countdown1.is_expired())
    print()
    print(countdown2.time_left())
    print(countdown2.is_expired())
    print()
    print(countdown3.time_left())
    print(countdown3.is_expired())

main()