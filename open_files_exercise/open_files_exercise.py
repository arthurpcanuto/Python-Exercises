#We use input() to get the file name of the file user wants to read through.
file_name = input("Enter a file name: ")


#We use open() to assign this variable the file handle, hence why it is called (fhand).
fhand = open(file_name)

#Basic loop to print the file's content in uppercase.
for line in fhand:
    print(line.upper())