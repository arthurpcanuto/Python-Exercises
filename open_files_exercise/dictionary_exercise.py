print("\nThis is a simple exercise to better understand dictionaries.")

# An input so user can give the file he wishes to use.
file_name = input("What is the file name? ")

# This variable stores the file handle.
try:
    fhand = open(file_name)
except:
    print("Wrong file name.")
    quit()

counts = {}
for line in fhand:
    # This removes the extra spaces on the end of the lines.
    line = line.rstrip()
    # We split the lines and get a list of words.
    word_list = line.split()
    # This loop will count each word from (word_list) and assign a key-value containing the word and word count.
    for word in word_list:
        counts[word] = counts.get(word, 0) + 1

    # Variables to set up our loop.
    bigcount = None
    bigword = None
    # This loop will go through each key-value created on the previous loop and
    # pick the one where the number associated with a word is the biggest one.
    # Then it will store both the word and the number on our variables so we can print it out.
    for word, count in counts.items():
        if bigcount is None or count > bigcount:
            bigword = word
            bigcount = count

print(bigword, bigcount)
