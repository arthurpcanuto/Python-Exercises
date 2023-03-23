print("Welcome to this simple calculator. First you will enter a number, this will be the number that"\
     + " you will subtract from, add to, or divide by. You get it. The rest is self explanatory. Good luck.\n")

num1 = input("Please enter the first number: ")
operator = input("Please enter the operator: Ex. (+, -, /, *): ")
num2 = input("Please enter the second number: ")

try:
    num1 = float(num1)
    num2 = float(num2)
except ValueError:
    print('Please input a valid number.')
    quit()

if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    result = num1 / num2
else:
    print("Invalid operator.")

print('Result:', result)
