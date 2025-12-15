n= int(input())
msg= ""
for i in range(1,n+1):
    if i==n:
        msg += str(i)
        break
    msg += str(i) + " "
print(msg)    