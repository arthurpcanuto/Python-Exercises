import random

#This function check to see if the user input a letter, if user didn't it prompts user to do so.
def inputcheck(letter):
    while not letter.isalpha():
        print('\nPlease enter a valid letter.')
        letter = input('Please enter a letter: ')
    return letter

tries = 6
Playing = True


#Initial message.
print('Welcome to my hangman game, it will generate a random word from a dictionary and I hope you know how'
      ' to play hangman because I do not wnat to explain here!')

input('\nPress enter to start!')

#This is the list of words for the game.
words = ['about', 'after', 'again', 'airplane', 'almost', 'already', 'always', 'another', 'answer', 'anyone', 'anything', 'around', 'beautiful', 'because', 'before', 'behind', 'believe', 'between', 'bicycle', 'billion',
         'business', 'calendar', 'camera', 'capital', 'careful', 'carrot', 'center', 'century', 'certain', 'chance', 'change', 'check', 'chicken', 'church', 'circle', 'citizen', 'coffee', 'college', 'company', 'computer',
         'consider', 'continue', 'control', 'correct', 'country', 'courage', 'create', 'cultural', 'customer', 'danger', 'daughter', 'decide', 'defense', 'delight', 'democracy', 'develop', 'diamond', 'difference', 'difficult',
         'dinner', 'direction', 'discover', 'distance', 'diverse', 'doctor', 'document', 'domestic', 'doorway', 'downtown', 'dragon', 'dramatic', 'economy', 'education', 'election', 'electric', 'element', 'elevator', 'embrace',
         'emotion', 'employee', 'engine', 'enough', 'enter', 'entire', 'environment', 'equal', 'escape', 'especially', 'establish', 'event', 'everybody', 'everyone', 'everything', 'everywhere', 'exactly', 'excellent', 'exciting',
         'exercise', 'existing', 'expensive', 'experience', 'explain', 'expression', 'familiar', 'family', 'famous', 'favorite', 'federal', 'fifteen']



while Playing is True:
    #Here we randomly select a word from the list.
    random_word = random.choice(words)
    #Here we count how many letters the word has.
    letter_count = int(len(random_word))

    #This prints out a number of (_) equal to the number of letters in the word.
    for i in range(letter_count):
        print('_ ', end="")

    #This creates our (letter) variable then we use our inputcheck() fucntion to see if it is a valid letter.
    letter = input('\nPlease enter a letter: ')
    letter = inputcheck(letter)

    #This and the following (if) statement only exist for testing.
    stop = input('\nY to stop: ')

    if stop == "Y":
        Playing = False


