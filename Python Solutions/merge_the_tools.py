import textwrap

def merge_the_tools(string, k):
    # your code goes here
    lst=textwrap.wrap(string,k)
    for i in lst:
        print("".join(dict.fromkeys(i)))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)