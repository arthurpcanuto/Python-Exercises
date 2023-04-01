# This is an exercise that asks us to write a function so it can determine
# the color of a chess board square. The board runs from 0 to 7 in both rows
# and columns. (0, 0) is always white.


# This function will determine first if the number combination is inside the board,
# then it will check to see if the sum of both numbers is even or odd, if it is even
# then it is white, since (0, 0) is always white that means that every even
# number sum is white. It also takes care of negative numbers.
def getChessSquareColor(column, row):
    if column > 7 or row > 7:
        return ""
    elif column < 0 or row < 0:
        return "C'mon there's no negative numbers in a chess board."
    elif (column + row) % 2 == 0:
        return "white"
    else:
        return "black"


# Some tests to check if the code above is correct.
assert getChessSquareColor(1, 1) == "white"
assert getChessSquareColor(2, 1) == "black"
assert getChessSquareColor(1, 2) == "black"
assert getChessSquareColor(7, 7) == "white"
assert getChessSquareColor(0, 8) == ""
assert getChessSquareColor(2, 9) == ""

# This prints out if all tests are succesful.
print("All systems go!")
