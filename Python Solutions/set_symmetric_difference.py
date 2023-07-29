if __name__ == "__main__":
    # Enter your code here. Read input from STDIN. Print output to STDOUT
    n = int(input())
    n_roll = set(map(int, input().split()))
    b = int(input())
    b_roll = set(map(int, input().split()))
    
    print(len(n_roll.symmetric_difference(b_roll)))