#!/bin/python3
#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#
def timeConversion(s):
    # Write your code here
    if s.endswith("AM") or s.endswith("am"):
        if int((s.split(":"))[0]) == 12:
            print("{:02d}".format(int((s.split(":"))[0])-12)+":"+s.split(":")[1]+":"+s.split(":")[2][:-2])
        else:
            print("{:02d}".format(int((s.split(":"))[0]))+":"+s.split(":")[1]+":"+s.split(":")[2][:-2])    
    elif s.endswith("PM") or s.endswith("pm"):
        if int((s.split(":"))[0]) == 12:
            print("{:02d}".format(int((s.split(":"))[0]))+":"+s.split(":")[1]+":"+s.split(":")[2][:-2])    
        else:    
            print(str(int((s.split(":"))[0])+12)+":"+s.split(":")[1]+":"+s.split(":")[2][:-2])
    
if __name__ == '__main__':
    s = input()
    timeConversion(s)
