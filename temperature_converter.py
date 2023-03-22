# Asks user to input the temperature in fahrenheit.
tempf = input('Enter the temperature in Fahrenheit: ')
tempf = float(tempf)

# Turns fahrenheit into celsius and celsius into kelvin.
tempc = (tempf - 32) * 5/9
tempk = tempc + 273.15

# Formats the string so it only displays the first float number rounded up.
formatted_celsius = "{:.1f}".format(tempc)
formatted_kelvin = "{:.1f}".format(tempk)

# Prints out our results.
print('You entered the following temperature:', tempf)
print('Your temperature in ºC is', formatted_celsius)
print('Your temperature in ºK is', formatted_kelvin)
