import math

a= float(input())
b= float(input())
c= float(input())
n= ((b)**2)-(4*a*c)

if n ==0:
    x= -b/(2*a)
    print(f"R = {round(x,2)}")
elif n > 0:
    n= math.sqrt(n)
    r_1= (-b + n)/(2*a)
    r_2= (-b - n)/(2*a)
    print(f"R1 = {round(r_1,2)}")
    print(f"R2 = {round(r_2,2)}")
else:
    n= math.sqrt(-n)/(2*a)
    r_1= -b/(2*a)
    print(f"R1 = {round(r_1,2)} + {round(n,2)}i")
    print(f"R2 = {round(r_1,2)} - {round(n,2)}i")