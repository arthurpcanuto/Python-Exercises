# We ask user to input the total hours user works and how much user gets paid.
totalHours = input('How many hours do you work? ')
pay = input('How much do you get paid per hour? ')

# We float both number we got above.
totalHours = float(totalHours)
pay = float(pay)

# We calculate user's total pay, then we string it (unnecessarily as I since learned).
totalPay = totalHours * pay
totalPay = str(totalPay)

# We print out how much user gets paid.
print('You get paid this much:', totalPay)
