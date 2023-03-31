# This for a function to display the ASCII number and
# Its corresponding text character, from 32 to 126.


# This function will take a number from 32 to 126 and
# print out the ASCII character corresponding to that number.
def printASCII_table():
    for i in range(32, 126 + 1):
        print(i, chr(i))

# We call our function for the program to run.
printASCII_table()