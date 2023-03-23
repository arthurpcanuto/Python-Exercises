import random

rolls = input(
    "How many times do you want to roll? Choose a value between 1 and 5: ")

try:
    rolls = float(rolls)

except ValueError:
    print("Please input a valid number.")
    quit()

# This only exists in case user tries to roll the dice 3.5 times, for example.
int_rolls = int(round(rolls))

# This is effectively our dice, since it will randomize a number between 1 and 6 and assign it to (dice).
# Yes, I realize it doesn't need to be here, but I'm mainly writing this notes to myself, and this
# Helps me out later when revewing the code when studying.
dice = random.randint(1, 6)

# Again, I don't know functions or loops yet. This probably looks reidiculous, but it works. \_(-_-)_/
if int_rolls == 1:
    dice = random.randint(1, 6)
    print(dice)
elif int_rolls == 2:
    dice = random.randint(1, 6)
    print(dice)
    dice = random.randint(1, 6)
    print(dice)
elif int_rolls == 3:
    dice = random.randint(1, 6)
    print(dice)
    dice = random.randint(1, 6)
    print(dice)
    dice = random.randint(1, 6)
    print(dice)
elif int_rolls == 4:
    dice = random.randint(1, 6)
    print(dice)
    dice = random.randint(1, 6)
    print(dice)
    dice = random.randint(1, 6)
    print(dice)
    dice = random.randint(1, 6)
    print(dice)
elif int_rolls == 5:
    dice = random.randint(1, 6)
    print(dice)
    dice = random.randint(1, 6)
    print(dice)
    dice = random.randint(1, 6)
    print(dice)
    dice = random.randint(1, 6)
    print(dice)
    dice = random.randint(1, 6)
    print(dice)
else:
    print("Please enter a valid number.")
    quit()
