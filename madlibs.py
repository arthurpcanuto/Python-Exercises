# Here we just request that the user presses enter to start the program.
input("Welcome to my simple madlibs game. Press enter to start.")

# You may be wondering why I don't use a function to get the multiple inputs without repeating the same code.
# Well, at this point I haven't learned functions yet. I'm on the "conditions" part of this journey to learn Python.
verb = input("First word, this should be a verb: ").lower()
noun = input("Second word, please enter a noun: ").lower()
adjective = input("Third word, please enter an adjective: ").lower()

# Nested (try) conditions to avoid using loops (that I haven't learned yet).
# The objective is simply to make sure that user doesn't input a number.
try:
    float(verb)
    print("Looks like you've entered a number for a verb, please use only words.")
except ValueError:
    try:
        float(noun)
        print("Looks like you've entered a number for a noun, please use only words.")
    except ValueError:
        try:
            float(adjective)
            print(
                "Looks like you've entered a number for an adjective, please use only words.")
        except ValueError:
            input("Very good. Please press enter to see the generated sentence.")

            # Turns out that nested (try) conditions are really limiting, I'm excited for loops now.

            # Here we concatenate our madlibs.So we can print it later for the user.
            madlibs = '\nA vacation is when you take a trip to some ' + adjective + ' place. Usually you go to some place that is near a ' \
                + noun + '. Those places are pretty ' + adjective + "." + " Turns out I don't use your verb word '" + verb \
                    +"' because writing madlibs is harder than coding." 

            print(madlibs)
