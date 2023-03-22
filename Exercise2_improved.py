# We ask user to input the total hours user works and
# how much user gets paid per hour. Then we float those inputs.
total_hours = float(input('How many hours do you work? '))
pay = float(input('How much do you get paid per hour? '))

# Here we define how many extra hours beyond 40 the user works
if total_hours > 40:
    extra_hours = total_hours - 40
elif total_hours <= 40:
    extra_hours = 0

# Here we calculate the user's total pay taking into consideration that
# every hour above 40 has extra pay.
total_pay = (40 * pay) + (extra_hours * (1.5*pay))

print('You get paid this much:', total_pay)
