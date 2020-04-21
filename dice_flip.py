
# We have a set of 6-sided dice, each showing a given face. We can rotate the dice so that they show
# neighboring faces - flipping a dice onto the opposite face takes two rotations. The opposite faces
# of a 6-sided die sum up to 7. The task is as follows: find the minimum number of rotations required,
# so that all dice show the same face, any of the six.

# Solution uses dynamic programming. We keep an array whose rows represent the amount of dice considered,
# and columns represent the face we are rotating to. The values are the amounts of rotations needed. The
# ultimate result is the minimum value in the bottom row.


def dice_flip(dice_list):
    dice_count = len(dice_list)
    # initialize array
    flip_amount = [[0 for j in range(dice_count + 1)] for i in range(6)]
    for i in range(6):
        flip_amount[i][0] = 0
    # run dynamic algorithm
    for i in range(6):
        for j in range(1, dice_count + 1):
            # case 1: we need to flip the die to the opposite face
            if i + 1 + dice_list[j - 1] == 7:
                flip_amount[i][j] = flip_amount[i][j - 1] + 2
            # case 2: the die is on the right face
            elif i + 1 == dice_list[j - 1]:
                flip_amount[i][j] = flip_amount[i][j - 1]
            # case 3: the die is on one of the neighboring faces
            else:
                flip_amount[i][j] = flip_amount[i][j - 1] + 1
    # result is the minimum of the bottom row
    return min(flip_amount[0][dice_count], flip_amount[1][dice_count], flip_amount[2][dice_count],
               flip_amount[3][dice_count], flip_amount[4][dice_count], flip_amount[5][dice_count])


if __name__ == "__main__":
    A = [1, 2, 3]
    B = [1, 1, 6]
    C = [1, 6, 2, 3]
    print(dice_flip(A))
    print(dice_flip(B))
    print(dice_flip(C))
