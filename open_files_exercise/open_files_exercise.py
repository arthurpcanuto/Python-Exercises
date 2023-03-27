#We use input() to get the file name of the file user wants to read through.
file_name = input("Enter a file name: ")


#We use open() to assign this variable the file handle, hence why it is called (fhand).
fhand = open(file_name)


for line in fhand:
    #This removes the extra spaces on the end of the lines.
    line = line.rstrip()
    #If the line does not start with 'From' the loop skips to its next iteration.
    if not line.startswith("From ") : continue
    #This splits the string (line) everytime there is a space(' '), and makes a list out of the words in that line.
    words = line.split()
    #This prints the third word stored in the variable (words).
    print(words[2])
