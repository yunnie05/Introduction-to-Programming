def factorial(n):
    if n==0:
        return 1
    return n * factorial(n-1)


def combination(n,k):
    if k <= n: 
        return int(factorial(n)/(factorial(k)*factorial(n-k)))
    return "NA"