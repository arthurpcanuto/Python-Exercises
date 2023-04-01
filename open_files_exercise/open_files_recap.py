# This is a simple exercise to learn how to write, append and read from a file.


# This function will write to a file. It takes two parameters:
# (fileName) which is the name you want to give, or already have, of the file and
# (text) which is the text you want to write to the file.
def writeToFile(fileName, text):
    # The (with) statement creates a context manager, it runs the code and then
    # automatically perform clean up tasks, in this case closing the file after we
    # write to it.
    with open(fileName, "w") as file:
        file.write(text)


# This function will append to the file, in this case it takes the same parameters that
# (writeToFile) takes. Different from writing appending does not overwrite the contents
# of the file.
def appendToFile(fileName, text):
    with open(fileName, "a") as file:
        file.write(text)


# This function will read whatever is inside the file and output it as a string.
# It takes one parameter (fileHandle) which is the handle of the file.
def readFromFile(fileHandle):
    with open(fileHandle, "r") as file:
        content = file.read()

        return content


# Some tests to see if the code works.
writeToFile("greet.txt", "Hello!\n")
appendToFile("greet.txt", "Goodbye!\n")
assert readFromFile("greet.txt") == "Hello!\nGoodbye!\n"

print("It works.")
