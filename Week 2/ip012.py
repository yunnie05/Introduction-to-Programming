n= int(input())
for i in range(1,n+1):
    answer= ""
    if i % 3==0:
        answer += "Fizz"
        if i % 5==0:
            answer+= "Buzz"  
    elif i % 5==0:
        answer += "Buzz"  
    else:
        answer=i      
    print(answer)