# This checks to see if the number is fractional, even or odd.
def check_number(number):
    if number % 1 != 0:
        return "fractional"
    elif number % 2 == 0:
        return "even"
    else:
        return "odd"


#Some tests to check if the code works.
def test_check_number():
    assert check_number(2) == "even"
    assert check_number(3) == "odd"
    assert check_number(0) == "even"
    assert check_number(-2) == "even"
    assert check_number(-3) == "odd"
    assert check_number(2.5) == "fractional"
    assert check_number(-2.5) == "fractional"
    assert check_number(0.1) == "fractional"
    print("All tests passed!")

test_check_number()


# This exists only for user to start the program.
input("\nWanna cheack if a number is odd or even? Press enter.\n")


# Our main function, the program's logic.
def main():
    # Try block to check if the user input was correct, if not we quit.
    try:
        number = float(input("\nInput your number: "))
    except:
        print("Please enter a valid number.")
        quit()

    numcheck = check_number(number)

    if numcheck == "fractional":
        print("I'm sorry, I don't know how to check fractionals yet.\n")
    else:
        print("\nThe number is " + numcheck.capitalize() + "!")


# Control variable for our main loop.
checking = True
# Our main loop.
while checking is True:
    main()
    # User decides if he wants to check more numbers.
    again = input(
        "Do you wanna check another number? Enter 'yes' to check another number. ")

    # We either close the loop and the program or continue, depends on user's decision.
    if again.lower() != "yes":
        checking = False

