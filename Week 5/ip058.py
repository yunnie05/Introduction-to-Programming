def factorial(n):
    if n==0:
        return 1
    return n * factorial(n-1)

def pascal(n):
    res= []
    for i in range(n):
        res.append(factorial(n-1)//(factorial((n-1)-i)*factorial(i)))
    return res