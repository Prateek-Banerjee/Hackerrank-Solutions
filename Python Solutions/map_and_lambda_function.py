cube = lambda x: x**3# complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    a,b,c = -1,1,list()
    for i in range(1,n+1):
        c.append(a+b)
        a,b=b,(a+b)
    return c

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))