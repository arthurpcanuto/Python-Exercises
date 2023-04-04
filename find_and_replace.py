# This is a find and replace exercise.
# The exercise does ask us to not use the string methods
# find(), replace() and index() as they can make the task trivial.


# This is the function that will do what the exercise requires.
# It takes three parameters, them being the orignal text (text),
# The text we wish to replace (oldText), and the replacement text (newText).
def findAndReplace(text, oldText, newText):
    # We create an empty list so we can append our modified text to it.
    replaced_text = []

    # We initialize our counter.
    i = 0
    # The loop must not run beyond the legnth of our orignal text (text).
    while i < len(text):
        # This is a moving slice, the indexes are (i) and (i + len(oldText))
        # this is because we want to make sure we match the slice legnth to the
        # length of the text we wish to replace. When we find a match we append
        # the replacement text to the list in the (oldText) position.
        # We then increment (i) by the (len(oldText)) because there's no point
        # reiterating over these letters as we already found a match.
        if text[i : i + len(oldText)] == oldText:
            replaced_text.append(newText)
            i = i + len(oldText)
        # If we do not find a mathch then we increment (i) by one, so we move our slice up the string.
        # While we do this we append each index to the list (replaced_text) so at the end we will have
        # the complete text and not only the text that was replaced on the previous step.
        elif text[i : i + len(oldText)] != oldText:
            replaced_text.append(text[i])
            i += 1

    # We join the elements of the list into a string.
    replaced_text = "".join(replaced_text)
    # The function returns our string with the new text.
    return replaced_text


# Some tests to see if the code above works as intended.
assert findAndReplace("The fox", "fox", "dog") == "The dog"
assert findAndReplace("fox", "fox", "dog") == "dog"
assert findAndReplace("Firefox", "fox", "dog") == "Firedog"
assert findAndReplace("foxfox", "fox", "dog") == "dogdog"
assert findAndReplace("The Fox and fox.", "fox", "dog") == "The Fox and dog."

print("It works!!")
