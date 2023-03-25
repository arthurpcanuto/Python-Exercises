#This is a random string given by the teacher for the exercise.
str = 'X-DSPAM-Confidence: 0.8475 '

#This will find the character so we can slice the string on the right point.
found = str.find(' ')

#This is the sliced string.
new_string = str[found + 1:]

#Here we float the number.
number = float(new_string)

#Here we print to check if we did everything right.
print(new_string)

#I guess you could also write it like this:
numberx = float(str[str.find(':') + 1:])
print(numberx)