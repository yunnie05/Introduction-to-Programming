n= int(input())
msg= str(n)
for i in range(n+1,101):
    if i % n==0:
        msg += " " + str(i) 
print(msg)