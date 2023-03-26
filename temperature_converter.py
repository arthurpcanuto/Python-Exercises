
# This function will handle the conversion tasks.
def temp_converter(temperature, scale):
    if scale.lower() == "k":
        temperature_c = temperature - 273.15
        temperature_f = temperature_c * (9/5) + 32
        temperature_k = temperature

    elif scale.lower() == "f":
        temperature_c = (temperature - 32) * (5/9)
        temperature_k = (temperature_c + 273.15)
        temperature_f = temperature

    elif scale.lower() == "c":
        temperature_k = temperature + 273.15
        temperature_f = temperature * (9/5) + 32
        temperature_c = temperature

    return temperature_c, temperature_f, temperature_k

# This function will take the returns from (temp_converter) format and print them.


def temperature_print(temperature_c, temperature_f, temperature_k):
    formattted_celsius = "{:.2f}".format(temperature_c)
    formatted_fahrenheit = "{:.2f}".format(temperature_f)
    formatted_kelvin = "{:.2f}".format(temperature_k)

    print("Your temperature in Celsius is:", formattted_celsius)
    print("Your temperature in Fahrenheit is:", formatted_fahrenheit)
    print("Your temperature in Kelvin is:", formatted_kelvin)


# Our welcome message.
print("Welcome to my improved temperature converter!\n")

# This function is the program itself.


def main():
    # Here we take the user's choice.
    choice = input(
        "Please type which temperature you would like to convert(e.g., 25 C, 77 F, 100 K): ")

    # We check to see if user inserted the temperature correctly then we split and float the number value.
    # If user didn't we print an error message and then quit.
    try:
        temperature, scale = choice.split()
        temperature = float(temperature)
    except ValueError:
        print("Please input a valid number, remember to separate number and scale like in the examples.")
        quit()

    # We assign the output of (temp_converter) to a variable so we can pass that output to (temperature_print).
    converted_temperatures = temp_converter(temperature, scale)
    temperature_print(*converted_temperatures)


# Control variable for the loop.
convert_again = True

# Main loop.
while convert_again:
    # This calls our (main) function so the program runs.
    main()

    # This prompts the user to decide if he wants to convert more temperatures.
    user_decision = input(
        "\nWould you like to convert temperatures again? Enter 'yes' to convert again. ")

    # If user answers anything other than (yes) we stop the loop.
    if user_decision.lower() != 'yes':
        convert_again = False

print("\n Thank you for using my program.")
