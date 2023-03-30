# Exercise to take a number and return a string of the number with its ordinal suffix
# It explicitly forbids the use of the endswith() method or it would be too easy.


# Here we define our function (ordinalSuffix)
def ordinalSuffix(number):
    # A list of our suffixes.
    suffixes = ["st", "nd", "rd", "th"]
    # We turn the number into a string so we can get the last digit character index,
    # Then we store it into (last_digit)
    number_string = str(number)
    last_digit = int(number_string[-1])

    # I'm not proud about how long I took to come up with this.
    # These conditionals check to see if the number ends with 11, 12 or 13.
    # However the first statement will not work on numbers bigger than 100,
    # So we need the second one to catch any number bigger than 100 to infinite,
    # However the second statement will not catch any number lower than 100, so yeah, we need both.
    # Also, if we wrote this in a single line with (or) it would always be true (for some reason I don't yet understand),
    # So I wrote it like this, when I improve I'll come back to fix this thing, I'm sure there's a better way to do this.
    if number_string in ("11", "12", "13"):
        return number_string + suffixes[3]
    elif number_string[-2:] in ("11", "12", "13"):
        return number_string + suffixes[3]

    # This was a lot simpler to write than the first block of conditionals.
    # It simply checks to see if the number ends in 1, 2 or 3 and concatenates the
    # appropriate suffix to the string containing the number.
    if last_digit == 1:
        return number_string + suffixes[0]
    elif last_digit == 2:
        return number_string + suffixes[1]
    elif last_digit == 3:
        return number_string + suffixes[2]
    else:
        return number_string + suffixes[3]


# Some test to see if the code works.
assert ordinalSuffix(0) == "0th"
assert ordinalSuffix(1) == "1st"
assert ordinalSuffix(2) == "2nd"
assert ordinalSuffix(3) == "3rd"
assert ordinalSuffix(4) == "4th"
assert ordinalSuffix(10) == "10th"
assert ordinalSuffix(11) == "11th"
assert ordinalSuffix(12) == "12th"
assert ordinalSuffix(13) == "13th"
assert ordinalSuffix(14) == "14th"
assert ordinalSuffix(101) == "101st"
assert ordinalSuffix(111) == "111th"
print("All systems go.")


# Here we get the user input an check to see if it is an integer.
try:
    number = int(input("Input your number here: "))
except:
    print("Please input a valid number, only integers are valid.")
    quit()

# We call our function and store its return on the variable (ordinal).
ordinal = ordinalSuffix(number)

# We print out the final ordinal number to the user.
print("Your ordinal number is:", ordinal)

# This was harder then expected fml. I love methods now.
