# This will check if the user's input is valid.
def get_integer_input(prompt):
    while True:
        try:
            number = int(input(prompt))
            return number
        except:
            print("Sorry only integers are supported.")

# This is our main fizzBuzz function, it takes the user's input, creates a list
# from 1 up to the user's input then we use a for loop to check the conditions
# after the check we append FizzBuzz, Fizz, Buzz or the number to an empty list
# then we print out the list to the user. The exercise did require it all be done
# in the same function.


def fizzBuzz(up_to):
    number_list = list(range(1, up_to + 1))
    output_list = []
    for fizzbuzz in number_list:
        if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
            output_list.append("FizzBuzz")
        elif fizzbuzz % 3 == 0:
            output_list.append("Fizz")
        elif fizzbuzz % 5 == 0:
            output_list.append("Buzz")
        else:
            output_list.append(fizzbuzz)

    print(output_list)


# We assign the user's input to the variable (up_to).
up_to = get_integer_input("Please input a number: ")
# We call our function and pass in the variable we assigned to our user's input number.
fizzBuzz(up_to)
