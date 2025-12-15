import math

def digits_average(n):
    while n%10!=0:
      if (len(str(n)))==1:
          break
      aux= 0
      for i in range(len(str(n))-1):
          x= n%100
          aux += math.ceil((x//10 + x % 10)/2)* 10**i
          n= n//10 
      n= aux 
    return n

