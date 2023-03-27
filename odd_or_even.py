#This checks to see if the number is an odd one.
def isOdd(number):
    if number % 2 == 1:
        return True
    elif number % 2 != 1:
        return False
    else:
        return False
#This checks to see if the is an even one.
def isEven(number):
    if number % 2 == 0:
        return True
    elif number % 2 != 0:
        return False
    else:
        return False

#This exists only for user to start the program.
input("\nWanna cheack if a number is odd or even? Press enter.\n")


#Our main function, the program's logic.
def main():
    #Try block to check if the user input was correct, if not we quit.
    try:
        number = float(input("\nInput your number: "))
    except:
        print("Please enter a valid number.")
        quit()

    #Variables to store the output of our functions.
    numcheck_Odd = isOdd(number)
    numcheck_Even = isEven(number)

    #After checking to see if the number is even or odd with our functions, we use this to
    #print out the result for user to see. We also return a message if user entered a fractional number.
    if numcheck_Odd == True:
        print("\nThe number is Odd!")
    elif numcheck_Even == True:
        print("\nThe number is Even!")
    else:
        print("I'm sorry, I don't know how to check fractionals yet.\n")


#Control variable for our main loop.   
checking = True
#Our main loop.
while checking is True:
    main()
    #User decides if he wants to check more numbers.
    again = input("Do you wanna check another number? Enter 'yes' to check another number. ")

    #We either close the loop and the program or continue depending on user's decision.
    if again.lower() != "yes":
        checking = False