print("\nThis is a simple exercise to better understand tuples.")

# User inputs file he wishes to read.
file_name = input("What is the file name? ")

# We test to see if user's input file name is valid.
try:
    fhand = open(file_name)
except:
    print("Sorry, wrong file name.")
    quit()

# We create the dictionary counts.
counts = {}

# In this loop we read through each line of the file,
# then we strip the empty spaces at the end of these lines,
# then we create a list containing the words in each line.
for line in fhand:
    line = line.rstrip()
    word_list = line.split()

    # In this loop we take each word in the (word_list) list and
    # we assign a number value to them, then we put thse key-value
    # pairs inside our dictionary (counts).
    for word in word_list:
        counts[word] = counts.get(word, 0) + 1

# Here we create an empty list to store our tuples.
tuple_list = list()

# In this loop we invert the key-value types so we get value-key pairs.
# Then we store one of these tuples inside our (new_tuple) variable,
# append it to the list and repeat the process util we get a list
# containing all the inverted key-value types.
for key, val in counts.items():
    newtuple = (val, key)
    tuple_list.append(newtuple)

    # Here we sort the list in descending order, so we get the most common word first,
    # then the second most common word, etc.
    tuple_list = sorted(tuple_list, reverse=True)

# Here we print out the 5 most common words in our file along with their count.
for val, key in tuple_list[:5]:
    print(key, val)
