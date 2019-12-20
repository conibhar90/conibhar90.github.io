# author: Brian Cho
# date: 12/12/2019
# code description: function for solving the coding exercise problem

########################################################################################################################
# array_movement(a, x, y, movement_set)
# This function predicts the location of the cursor after going through a set of movement instructions represented
# in the string


def array_movement(a, x, y, movement_set):

    rows, columns = a, a

    array = [[0 for i in range(columns)] for j in range(rows)]
    array[x][y] = 1

    for i in range(len(movement_set)):

        if movement_set[i] == "U" and x != 0:

            array[x][y] = 0
            x -= 1
            array[x][y] = 1

        elif movement_set[i] == "D" and x != a - 1:

            array[x][y] = 0
            x += 1
            array[x][y] = 1

        elif movement_set[i] == "L":
            array[x][y] = 0
            y -= 1
            array[x][y] = 1
            if y < 0:
                y += 3

        elif movement_set[i] == "R":
            array[x][y] = 0
            y += 1
            array[x][y] = 1
            if y > a-1:
                y -= a

    print("[" + str(x) + ", " + str(y) + "]")


# test example: array_movement(3, 0, 0, "RDD")

