#Asks user to input the bill amount and the tip percentage.
bill = input('Enter how much was your restaurant bill: ')
tip_percentage = input('How much is the tip percentage? Enter only numbers: ')

#Floats the bill amount and the tip percentage.
bill = float(bill)
tip_percentage = float(tip_percentage)

#Calculates the tip total.
tip_total = (bill * tip_percentage)/100

#Formats tip_total to be more presentable.
formatted_tiptotal = "{:.2f}".format(tip_total)

#Adds the tip_total and bill together, to get total_bill.
total_bill = (bill + tip_total)

#Formats total_bill to be more readable.
formatted_totalbill = "{:.2f}".format(total_bill)

#Prints out the correct tip amount.
print('The total tip for this bill is:', formatted_tiptotal)
print('And the total bill (including tip) is:', formatted_totalbill)