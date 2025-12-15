n= int(input())
res=""
count= 1
num=""
comp_string= ((n-1)*2) +1 #tamanho da string
for i in range(1,n+1):
    for j in range(1,i+1):
          num += str(j)
    for j in range(i-1, 0,-1):
        num += str(j)
    x= (comp_string- len(num))//2
    res+=" "*x +num
    if(i!=n):
        res+= "\n"
    num= ""
print(res)