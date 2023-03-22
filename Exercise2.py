totalHours = input('How many hours do you work? ')
pay = input('How much do you get paid per hour? ')

totalHours = float(totalHours)
pay = float(pay)

totalPay = totalHours * pay
totalPay = str(totalPay)

print('You get paid this much:', totalPay)
