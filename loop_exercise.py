# Here we define some initial variables.
running = True
num_list = []
num_counter = 0

# Here we print a message so the user know how to use the prgram.
print("This is a number counter, enter a number and press the return key."
      " You can enter however many number you want, and in the end the program"
      " will tell you the sum and the number of number you entered.")


# This is my first loop. Hooray!
while running is True:
    num = (input("Please enter a number: "))

    # Here we ask if the input is different than 'done', so we know if we should finish the program or keep going.
    if num != 'done':
        # This (try) statement is to make sure the user inputs numbers, and that only numbers get put into our list and count to (num_counter).
        try:
            num = float(num)
            num_list.append(num)
            num_counter += 1
        except ValueError:
            print("\nPlease input a valid number or 'done' to finish.")

    # Here we check to see if user input 'done', if user did we sum all the numbers from the list,
    # make some basic operations and print out the info.
    if num == 'done':
        total_sum = sum(num_list)

        print("Here's your list of numbers:", num_list)
        print("Here is the sum of your list:", total_sum)
        print("Here is how many numbers you entered:", num_counter)
        print("Here is the average of your numbers:", (total_sum/num_counter))

        # This finishes the loop and consequently the program.
        running = False
