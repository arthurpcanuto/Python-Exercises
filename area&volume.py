

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

#This function will capture the user's input and return them as float numbers
#So now we can use them to calculate our result.
def values(choice):
    value_length = float(input("What is the length of your shape? "))
    value_width = float(input("What is the width of your shape? "))
    
    if choice == "area" or choice == "perimeter":
        return value_length, value_width
    
    elif choice == "volume" or choice == "surface area":
        value_height = float(input("What is the height of your shape?"))
        return value_length, value_width, value_height

#This function will take care of calculating our result.
def result(choice, returned_values):
    if choice == "area":
        area_result = area(*returned_values)
        print(area_result)
    elif choice == "perimeter":
        perimeter_result = perimeter(*returned_values)
        print(perimeter_result)
    elif choice == 'volume':
        volume_result = volume(*returned_values)
        print(volume_result)
    else:
        surfaceArea_result = surface_area(*returned_values)
        print(surfaceArea_result)





print("\nThis program calculates the area, volume, perimeter and surface area of the "\
"retangles and retangular prisms. Yes, it does include cubes.")

#This is our main function and the program's logic.
def main():
    #This variable defines the valid inputs for user.
    valid_choices = ["area", "perimeter", "volume", "surface area"]
    
    #This loop checks if user's choice is valid, if it isn't it prompts user to choose again.
    while True:
        choice = input("\nPlease choose what you would like to calculate (e.g. area, perimeter, volume or surface area):")
        
        
        if choice.lower() in valid_choices:
            input("\n" + choice.capitalize() + " it is! Press enter to continue.")
            break
        else:
            print("Sorry, " + choice + " is not a valid choice. Please try again.")
    
    returned_values = values(choice)
    
    result(choice, returned_values)

            
main()
        




