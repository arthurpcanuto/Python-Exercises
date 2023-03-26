import random

# This function check to see if the user input a letter, if user didn't it prompts user to do so.


def inputcheck(letter):
    while not letter.isalpha():
        print('\nPlease enter a valid letter.')
        letter = input('Please enter a letter: ')
    return letter

# This function checks to see if the user inputted a correct letter, if user did it finds its place on the word
# and updates (guessed_word) to display it in its correct postion. If user didn't it deducts a try.


def letter_check(letter, random_word, guessed_word, tries):
    letter_found = False

    for index, char in enumerate(random_word.lower()):
        if char == letter.lower():
            guessed_word[index] = char
            letter_found = True

    if not letter_found:
        tries = tries - 1

    return guessed_word, tries


# Initial message.
print('Welcome to my hangman game, it will generate a random word from a dictionary and I hope you know how'
      ' to play hangman because I do not wnat to explain here!')

input('\nPress enter to start!')

# This is the list of words for the game.
words = ['about', 'after', 'again', 'airplane', 'almost', 'already', 'always', 'another', 'answer', 'anyone', 'anything', 'around', 'beautiful', 'because', 'before', 'behind', 'believe', 'between', 'bicycle', 'billion',
         'business', 'calendar', 'camera', 'capital', 'careful', 'carrot', 'center', 'century', 'certain', 'chance', 'change', 'check', 'chicken', 'church', 'circle', 'citizen', 'coffee', 'college', 'company', 'computer',
         'consider', 'continue', 'control', 'correct', 'country', 'courage', 'create', 'cultural', 'customer', 'danger', 'daughter', 'decide', 'defense', 'delight', 'democracy', 'develop', 'diamond', 'difference', 'difficult',
         'dinner', 'direction', 'discover', 'distance', 'diverse', 'doctor', 'document', 'domestic', 'doorway', 'downtown', 'dragon', 'dramatic', 'economy', 'education', 'election', 'electric', 'element', 'elevator', 'embrace',
         'emotion', 'employee', 'engine', 'enough', 'enter', 'entire', 'environment', 'equal', 'escape', 'especially', 'establish', 'event', 'everybody', 'everyone', 'everything', 'everywhere', 'exactly', 'excellent', 'exciting',
         'exercise', 'existing', 'expensive', 'experience', 'explain', 'expression', 'familiar', 'family', 'famous', 'favorite', 'federal', 'fifteen']


# This function is the game itself.
def main():
    # This is how many tries the user has.
    tries = 6
    # Here we randomly select a word from the list.
    random_word = random.choice(words)
    # This creates a string with a number of (_) equal to the number of letters in the word and stores it into (guessed_word)
    guessed_word = ['_'] * len(random_word)

    while tries > 0 and '_' in guessed_word:

        print(" ".join(guessed_word))
        print("\nTries left:", tries)

        # This creates our (letter) variable then we use our inputcheck() fucntion to see if it is a valid letter.
        letter = input('\nPlease enter a letter: ')
        letter = inputcheck(letter)

        guessed_word, tries = letter_check(
            letter, random_word, guessed_word, tries)

    # This is our win condition.
    if "_" not in guessed_word:
        print("\nCongratulations! You guessed the word!")
        print("The word was: '" + random_word + "'.")

    # This gets printed when user rans out of tries.
    else:
        print("Sorry, you ran out of tries. The word was '" + random_word + "'.\n")


play_again = True

# Our main loop.
while play_again:
    # This calls the main function to play the game.
    main()

    # This prompts the user to decide if he wants to play again.
    user_decision = input(
        "Would you like to play again? Enter 'yes' to play again. ")

    # If user answers anything other than (yes) we stop the loop.
    if user_decision.lower() != 'yes':
        play_again = False

print("\nThanks for playing!")
