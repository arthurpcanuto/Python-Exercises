import sys
import os
import subprocess

#Here we have the user input how many hours user works
#and how much does user make per hour.
total_hours = input('How many hours do you work? ')
pay = input('How much do you get paid per hour? ')

#Here we have a try statement, because user can make mistakes on the input,
#so we use this to not get a traceback, instead we print something useful for the user to know.
try:
    total_hours = float(total_hours)
    pay = float(pay)
except:
    total_hours = -1
    pay = -1
    print('Please input a valid number.')

#Here we define how many extra hours beyond 40 the user works.
if total_hours > 40:
    extra_hours = total_hours - 40
elif total_hours <= 40:
    extra_hours = 0

#Here we calculate the user's total pay taking into consideration
#that every hour above 40 has overtime pay.
total_pay = (40 * pay) + (extra_hours *(1.5 * pay))

#We use this if/else statement to give information to the user and restart the program
#if user made mistakes when user had to input his information.
if total_pay > 0:
    print('You get paid this much', total_pay)
else:
    print('You have input an invalid number, please double check.')

#I use this to restart the program, because I don't know how to use loops yet.
    subprocess.call([sys.executable, os.path.realpath(__file__)] +
                        sys.argv[1:])