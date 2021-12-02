def fibonacci(n):
    if n<=2:
        return n-1
    a=0
    c=1
    print("0")
    for i in range(3, n+1):
        b=c
        c=c+a
        a=b
        print(a)
    return c 


def fibonacci_sum(n):
    if n<=2:
        return n-1
    a=0
    c=1
    sum = 0
    for i in range(3, n+1):
        b=c
        c=c+a
        a=b
        sum+=a
    print(sum)
    return sum 
    

def fact(n):
    if n == 0:
        r = 1
    else:
        r = n * fact(n - 1)
    return r