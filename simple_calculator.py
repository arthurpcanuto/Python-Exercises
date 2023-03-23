print("Welcome to this simple calculator. First you will enter a number, this will be the number that"
      + " you will subtract from, add to, or divide by. You get it. The rest is self explanatory. Good luck.\n")
# Here we get the inputs from the user.
num1 = input("Please enter the first number: ")
operator = input("Please enter the operator: Ex. (+, -, /, *): ")
num2 = input("Please enter the second number: ")

# We use (try) to check if the numbers input are valid numbers.
try:
    num1 = float(num1)
    num2 = float(num2)
except ValueError:
    print('Please input a valid number.')
    quit()

# This is the calculator, I'm sure there must be a better way to this. Note to self: Come back to it eventually.
# If the user inputs a invalied operator we tell them and quit the program.
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
    quit()

# We print the result.
print('Result:', result)
