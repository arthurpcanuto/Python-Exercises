from decimal import Decimal


#This function will return the area.
def area(legnth, width):
    return (legnth * width)

#This function will return the perimeter.
def perimeter(length, width):
    return (length * 2) + (width * 2)

#This function will return the volume.
def volume(length, width, height):
    return (length * width * height)

#This function will return the surface area.
def surface_area(legnth, width, height):
    return (legnth * width * 2) + (legnth * height * 2) + (width * height * 2)

#This function will check if the user input is valid.
def check_Decimal_input(prompt):
    while True:
        try:
            value = Decimal(input(prompt))
            return value
        except ValueError:
            print("Please input a valid number.")

#This function will capture the user's input and return them as decimal numbers
#So now we can use them to calculate our result with precision.
def values(choice):
    #We call our function (check_Decimal_input) to check if user input is the correct type.
    value_length = check_Decimal_input("What is the length of your shape? ")
    value_width = check_Decimal_input("What is the width of your shape? ")
    
    if choice == "area" or choice == "perimeter":
        return value_length, value_width
    
    elif choice == "volume" or choice == "surface area" or choice == "surface":
        value_height = check_Decimal_input("What is the height of your shape? ")
        return value_length, value_width, value_height
    

#This function will take care of calculating our result.
def result(choice, returned_values):
    if choice == "area":
        area_result = area(*returned_values)
        print("\nThe area of your shape is:", area_result)
    elif choice == "perimeter":
        perimeter_result = perimeter(*returned_values)
        print("\nThe perimeter of you shape is:", perimeter_result)
    elif choice == 'volume':
        volume_result = volume(*returned_values)
        print("\nThe volume of your shape is:", volume_result)
    else:
        surfaceArea_result = surface_area(*returned_values)
        print("\nThe surface area of you shape is:", surfaceArea_result)




#Our initial message to the user.
print("\nThis program calculates the area, volume, perimeter and surface area of the "\
"retangles and retangular prisms. Yes, it does include cubes.")

#This is our main function and the program's logic.
def main():
    #This variable defines the valid inputs for user.
    valid_choices = ["area", "perimeter", "volume", "surface area", "surface"]
    
    #This loop checks if user's choice is valid, if it isn't it prompts user to choose again.
    while True:
        choice = input("\nPlease choose what you would like to calculate (e.g. area, perimeter, volume or surface area):")
        
        
        if choice.lower() in valid_choices:
            input("\n" + choice.capitalize() + " it is! Press enter to continue.")
            break
        else:
            print("Sorry, " + choice + " is not a valid choice. Please try again.")
    
    #We store the converted values from user input in this variable.
    returned_values = values(choice)
    
    #We call our result function to calculate based on user's choice and chosen values.
    result(choice, returned_values)




#Here we define a control function and initialize our main loop.
Calculating = True
while Calculating is True:            
    main()

    user_decision = input("Would you like to calculate something else? Enter 'yes' if yes. ")

    if user_decision.lower() != 'yes':
        Calculating = False

        




