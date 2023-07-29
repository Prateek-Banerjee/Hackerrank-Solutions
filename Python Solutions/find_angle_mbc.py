# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
if __name__ == "__main__":
    ab = int(input())
    bc = int(input())
    print(round(math.degrees(math.atan(ab/bc))),chr(176),sep="")