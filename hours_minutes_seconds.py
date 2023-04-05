# Here we import the decimal module so we can use it to make
# our results more accurate by avoiding floats.
from decimal import Decimal


# This is the function required by the exercise,
# it takes a number of seconds as input so it can return
# this number as days, hours, minutes and seconds.
def getHoursMinutesSeconds(totalSeconds):
    seconds = Decimal(totalSeconds)

    minutes = seconds // Decimal(60)
    hours = minutes // Decimal(60)
    days = hours // Decimal(24)

    excess_hours = hours % Decimal(24)
    excess_minutes = minutes % Decimal(60)
    excess_seconds = seconds % Decimal(60)

    # This is the list that will hold our output.
    output = []

    if days > 0:
        output.append(f"{days}d")

    if excess_hours > 0:
        output.append(f"{excess_hours}h")

    if excess_minutes > 0:
        output.append(f"{excess_minutes}m")

    if excess_seconds > 0 or (days == 0 and excess_hours == 0 and excess_minutes == 0):
        output.append(f"{excess_seconds}s")

    # We join the list into a string.
    return " ".join(output)


# Some tests to check if our code works.
assert getHoursMinutesSeconds(30) == "30s"
assert getHoursMinutesSeconds(60) == "1m"
assert getHoursMinutesSeconds(90) == "1m 30s"
assert getHoursMinutesSeconds(3600) == "1h"
assert getHoursMinutesSeconds(3601) == "1h 1s"
assert getHoursMinutesSeconds(3661) == "1h 1m 1s"
assert getHoursMinutesSeconds(90042) == "1d 1h 42s"
assert getHoursMinutesSeconds(0) == "0s"
print("Systems check.\n")


# Our main function containing the program's logic.
def main():
    try:
        user_seconds = Decimal(
            (input("\nInput the amount of seconds you wish to calculate: "))
        )
    except:
        print("\nPlease make sure to input a valid number.")
        quit()

    output_time = getHoursMinutesSeconds(user_seconds)
    print("\n" + output_time)


# A control variable for our main loop.
checking = True
# This is our main loop.
while checking is True:
    main()

    executing = input("\nWould you like to calculate again? Type 'yes' to continue: ")

    if executing.lower() != "yes":
        checking = False
