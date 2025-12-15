num= int(input())
soma= 0
fatores= ""
for i in range(num-1,0,-1):
    if(num%i==0):
        soma+= i
        fatores += " " + str(i)
if(num==soma):
    print(f"{num} is a perfect number")
    print(f"Factors:{fatores}")
else:
    print(f"{num} is not a perfect number")