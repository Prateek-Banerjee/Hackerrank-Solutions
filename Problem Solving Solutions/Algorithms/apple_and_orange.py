#!/bin/python3
#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#


def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    ca, co = 0, 0

    for i in apples:
        if a + i in range(s, t + 1):
            ca += 1
    for j in oranges:
        if b + j in range(s, t + 1):
            co += 1
    print(ca, "\n", co, sep="")


if __name__ == "__main__":
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])  # Sam's starting point

    t = int(first_multiple_input[1])  # Sam's ending point

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])  # Location of apple tree

    b = int(second_multiple_input[1])  # Location of orange tree

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])  # No. of apples

    n = int(third_multiple_input[1])  # No. of oranges

    apples = list(
        map(int, input().rstrip().split())
    )  # Distance of each apple from the tree

    oranges = list(
        map(int, input().rstrip().split())
    )  # Distance of each orange from the tree

    countApplesAndOranges(s, t, a, b, apples, oranges)
