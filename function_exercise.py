import os
import sys
import subprocess

# Here we have the user input how many hours user works
# and how much does user make per hour.
# We also have user input how much taxes does user pay.
total_hours = input('How many hours do you work? ')
pay = input('How much do you get paid per hour? ')
taxes = input("How much do you pay in taxes? If you don't just input 0: ")

# Here we have a try statement, because user can make mistakes on the input,
# so we use this to not get a traceback, instead we print something useful for the user to know.
try:
    total_hours = float(total_hours)
    pay = float(pay)
    taxes = float(taxes)
except ValueError:
    total_hours = -1
    pay = 1
    taxes = 0

# This function calculates everything now. Including taxes.


def compute_pay(hours, rate, tax):
    # Calculates overtime hours.
    if hours > 40:
        overtime = hours - 40
        hours = hours - overtime
    else:
        overtime = 0

    # Calculates total pay.
    paycompute = (hours * rate) + (overtime * (1.5 * rate))

    if tax > 0:
        # Calculate Tax.
        taxcompute = paycompute * (tax/100)
    else:
        tax = 0
        taxcompute = 0

    # Return total pay and tax.
    return paycompute, taxcompute


total_pay, total_taxes = compute_pay(total_hours, pay, taxes)

# We use this if/else statement to give information to the user and restart the program
# if user made mistakes when user had to input his information.
if total_pay > 0:
    print('\nYou get paid this much:', total_pay)
    print('Your total taxes are:', total_taxes)
    print('Your net pay is:', (total_pay - total_taxes))
else:
    print('You have input an invalid number, please double check.\n')

# I use this to restart the program, because I don't know how to use loops yet.
    subprocess.call([sys.executable, os.path.realpath(__file__)] +
                    sys.argv[1:])
