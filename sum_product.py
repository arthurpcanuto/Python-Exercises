# The exercise requires us to replicate the sum() funciton, so obviously it shouldn't be solved by using it.


# This function calculates the sum of a list of numbers (nums).
def calculateSum(nums):
    # If the list is empty we return 0.
    if len(nums) == 0:
        return 0

    # We define a variable that will be updated by the loop to hold
    # the value of the sum.
    total = 0

    # The loop runs through each number in the list and adds them to total.
    for n in nums:
        total += n

    # We return the result.
    return total


# This function calculates the product of a list of numbers (nums)
def calculateProduct(nums):
    # If the list is empty we retrun 1.
    if len(nums) == 0:
        return 1

    # We define a variable that will be updated by the loop to hold
    # the value of the pruduct.
    total = 1

    # The loop runs through each number on the list and multiplies them by the value in total.
    for n in nums:
        total *= n

    # We return the result.
    return total


# Tests for calculateSum
assert calculateSum([]) == 0
assert calculateSum([2, 4, 6, 8, 10]) == 30
assert calculateSum([]) == 0
assert calculateSum([1, 2, 3, 4, 5]) == 15
assert calculateSum([-1, 1, -2, 2, -3, 3]) == 0
assert calculateSum([5, 10, 15]) == 30
assert calculateSum([-5, 0, 5]) == 0

# Tests for calculateProduct
assert calculateProduct([]) == 1
assert calculateProduct([1, 2, 3, 4, 5]) == 120
assert calculateProduct([-1, 1, -2, 2, -3, 3]) == -36
assert calculateProduct([2, 3, 4]) == 24
assert calculateProduct([-2, 1, 2]) == -4
assert calculateProduct([]) == 1
assert calculateProduct([2, 4, 6, 8, 10]) == 3840

# This gets printed if the program passes all tests.
print("All systems go.")
