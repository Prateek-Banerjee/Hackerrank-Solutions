"""t = int(input())
for i in range(t):
    n = int(input())
    sideLengths = list(map(int, input().split()))

    if any(sideLengths[j]>sideLengths[len(sideLengths)-1] for j in range(len(sideLengths) - 1)): print("No")
    elif all(sideLengths[i] <= sideLengths[i+1] for i in range(len(sideLengths) - 1)):
        print("Yes")
    else: print("Yes")"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
t = int(input())
for i in range(t):
    n = int(input())
    sideLengths = list(map(int, input().split()))

    left, right = 0, n - 1
    prev_cube = float('inf')  # Initialize with positive infinity to handle the case when the pile is empty

    while left <= right:
        left_cube, right_cube = sideLengths[left], sideLengths[right]

        # Check if the current cube can be placed on top of the previous one
        if max(left_cube, right_cube) <= prev_cube:
            # Select the cube with the larger side length
            if left_cube >= right_cube:
                prev_cube = left_cube
                left += 1
            else:
                prev_cube = right_cube
                right -= 1
        elif left_cube <= prev_cube:
            prev_cube = left_cube
            left += 1
        elif right_cube <= prev_cube:
            prev_cube = right_cube
            right -= 1
        else:
            print("No")
            break
    else:
        print("Yes")
