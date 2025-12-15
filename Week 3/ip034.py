#while n!=1:
# if n%2==0: n+1= n/2
#else n+1= 3n+1

def collatz(n):
    re= str(n)
    while n!=1:
       if n%2==0: 
           n= n//2
       else:
           n= (3*n) +1
       re+= ", " + str(n)   
    list(re) 
    return re
