a= input()
a= a.split()
R= int(a[0])
k= int(a[1])
g= input() 

#1 converter R para binário

#2 criar um dicionário com 8 chaves

#conversor de binário 
def to_binary(var):
    ans= []
    if isinstance(var,int):
       while var!=0:
           if var!=0:
                ans.insert(0,var % 2)
                var= var//2
    elif isinstance(var,str):
        for i in var:
            if i == ".":
                ans.append(0)
            else:
                ans.append(1)
    return ans

def to_string(var):
    ans= ""
    for i in var:
        ans+= str(i)
    return ans

def keys(var):
    ans=[]
    x= 0
    for _ in range(len(var)):
        key= to_string(to_binary(x))
        if len(key) < 3:
            aux= 3 - len(key)
            key= "0"*aux + key
        ans.append(key)
        x+=1
    return ans
    
def dicti(var: list): #gera as chaves para cada string 000 010...
    aux= -1
    ans= {}
    x= 0
    ks= keys(var)
    ks.reverse()
    for i in ks:
        ans[i]= var[x]
        x+=1
    return ans

def automaton(fixed,g,left,center,right):#sequência binária segundo a regra
    #usando recursão
    new= ""
    join= left+center+right
    new = str(fixed[join])
    if len(g)==1:
        return new
    elif len(g)==2:
       new+= automaton(fixed,g[1:],g[0],g[1],"0")
    else:
       new += automaton(fixed,g[1:],g[0],g[1],g[2])
    #print(new)
    return new

def to_code(var):
    ans= ""
    for i in var:
        if i=="0":
            ans+= "."
        else:
            ans+= "#"
    return ans
        
def main(reg,k,g):
    a= to_binary(reg)
    if len(a)!=8:
        aux= 8 - len(a)
        for i in range(aux):
            a.insert(0,0)
    fixed= dicti(a)
    #print(fixed)
    g= to_string(to_binary(g))
    #print(fixed)
    while(k>0):
       #print(g)
       if len(g)==1:
           g= automaton(fixed,g,"0",g[0],"0")
       else:
           g= automaton(fixed,g,"0",g[0],g[1])
       #print(g)
       #ls= g[-2::1] + "0"
       #g+= str(fixed[ls])
       print(to_code(g))
       k-=1
    
    
main(R,k,g)
        
        