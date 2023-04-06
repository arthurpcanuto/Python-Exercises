# The exercise explicitly forbids the use of the
# min() and max() modules, or it would be trivial.


# This funciton will give us the smallest number in a list of ints or floats.
def getSmallest(numbers):
    # If for some reason the variable (numbers) is empty the funtion will retrun None.
    if len(numbers) == 0:
        return None

    # We create list so we can compare to the list (numbers) and store the smallest value.
    smallest = numbers[0]

    # This loop is the main logic. If (n) is smaller than the number in (smallest), it takes its place.
    for n in numbers:
        if n < smallest:
            smallest = n
    # We return the smallest number.
    return smallest


# This function will give us the biggest number in a list of ints or floats.
def getBiggest(numbers):
    # If for some reason (numbers) is empty the function will retrun None.
    if len(numbers) == 0:
        return None
    # We create a list so we can compare to the list (numbers) and store the biggest value.
    biggest = numbers[0]

    # This loop is the main logic. If (n) is bigger than the number in (biggest), it takes its place.
    for n in numbers:
        if n > biggest:
            biggest = n

    # We return the biggest number.
    return biggest


# Some tests to check if our function (getSmallest) works.
assert getSmallest([1, 2, 3]) == 1
assert getSmallest([3, 2, 1]) == 1
assert getSmallest([28, 25, 42, 2, 28]) == 2
assert getSmallest([1]) == 1
assert getSmallest([]) == None
print("Smallest check.")

# Some tests to check if our function (getBiggest) works.
assert getBiggest([1, 2, 3]) == 3
assert getBiggest([3, 2, 1]) == 3
assert getBiggest([28, 25, 42, 2, 28]) == 42
assert getBiggest([1]) == 1
assert getBiggest([]) == None
print("Biggest check.")
