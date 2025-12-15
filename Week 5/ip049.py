#returns a list with the first n numbers of the sequence

def fibonacci(a,b,n):
    fib= [a,b]
    for i in range(2,n):
        fib.append(fib[len(fib)-1]+fib[len(fib)-2])
    return fib