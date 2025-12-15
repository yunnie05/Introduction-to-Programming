def odd_even(tup):
    n= len(tup)
    even= ()
    odd = ()
    for i in range(n):
        if i % 2==0:
            odd += (tup[i],)
        else:
            even += (tup[i],)
    return odd+even 
