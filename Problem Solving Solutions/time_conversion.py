#!/bin/python3
#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#
def timeConversion(s):
    # Write your code here
    if (s.find("AM") != -1 and s.find("PM") != -1) or (s.find("am") != -1 and s.find("pm") != -1):
        if int((s.split(":"))[0]) > 12:
            print(str(int((s.split(":"))[0])-12)+":"+s.split(":")[1]+":"+s.split(":")[2]+"PM")
        elif int((s.split(":"))[0]) < 12:
            print(str((s.split(":"))[0])+":"+s.split(":")[1]+":"+s.split(":")[2]+"AM")
    elif s.find("PM") != -1:
        print(str(int((s.split(":"))[0])+12)+":"+s.split(":")[1]+":"+s.split(":")[2][:-2])

if __name__ == '__main__':
    s = input()

    timeConversion(s)