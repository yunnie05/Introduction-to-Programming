a= int(input())
b= int(input())
c= int(input())
maior= a
if maior < b or maior < c:
    if b > c:
        maior= b
    else:
        maior= c
print(maior)        