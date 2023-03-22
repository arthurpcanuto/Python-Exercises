import random
import sys
import os
import subprocess

# User inputs a number then we int it.
num = int(input('Guess a number between 1 and 10: '))

# Randomizes a number between 1 and 10, then defines it as correct_number.
correct_number = random.randint(1, 10)

# If user guesses right, we print "Congratulations you won!" and quit, if he guesses wrong he gets a choice to continue (y) or not (n), if he chooses (y) the program restarts and if he chooses (n) the program quits.
if num == correct_number:
    print('Congratulations you won!')
else:
    decision = input("I'm sorry you've lost. Play again? (y/n): ")
    if decision == 'y':
        subprocess.call([sys.executable, os.path.realpath(__file__)] + #We use this just to avoid using loops as I'v not learned it yet.
                        sys.argv[1:])
    if decision == 'n':
        quit
