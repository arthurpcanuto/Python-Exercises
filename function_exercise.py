import os
import sys
import subprocess

# Here we have the user input how many hours user works
# and how much does user make per hour.
total_hours = input('How many hours do you work? ')
pay = input('How much do you get paid per hour? ')

# Here we have a try statement, because user can make mistakes on the input,
# so we use this to not get a traceback, instead we print something useful for the user to know.
try:
    total_hours = float(total_hours)
    pay = float(pay)
except ValueError:
    total_hours = -1
    pay = -1
    print('Please input a valid number.')

# This function calculates if the user has overtime hours.


def compute_overtime(hours):
    if hours > 40:
        return hours - 40
    else:
        return 0


overtime = compute_overtime(total_hours)

# This function calculates the user's total pay.


def compute_pay():
    total_pay = (40 * pay) + (overtime * (1.5 * pay))
    return total_pay


total_pay = compute_pay()

# We use this if/else statement to give information to the user and restart the program
# if user made mistakes when user had to input his information.
if total_pay > 0:
    print('You get paid this much:', total_pay)
else:
    print('You have input an invalide number, please double check.')

# I use this to restart the program, because I don't know how to use loops yet.
    subprocess.call([sys.executable, os.path.realpath(__file__)] +
                    sys.argv[1:])
