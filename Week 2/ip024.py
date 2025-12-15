num= int(input())
result= 0
a= 10
while (num//a)!= 0:
    prim= num%a
    num=num//a
    seg= num%a
    if prim> seg:
        if result==2:
            result=0
            break
        result= 1
    elif prim < seg:
        if result==1:
            result=0
            break
        result=2   
if result==1:
    print("The number is in ascending order.")
elif result==2:
    print("The number is in descending order.")
else:
    print("The number is not ordered.")