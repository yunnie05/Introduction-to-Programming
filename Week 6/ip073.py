def possible(digits, a, b):
    ver= True
    min= str(a)[-1]
    max= str(b)[-1]
    digits= list(digits).sort()
    size= len(b)
    num= []
    lst= []
    if (len(str(a))<len(str(b))):
        num= []*(len(str(b))-len(str(a)))
        num.extend(str(a))
    else:
      num.extend(str(a))  
        
    for i in digits:#verifica se algum elemento de digits pode fazer 
        if (i in str(a)) or (i in str(b)):
            ver= False
    if ver:
        return 0
    return len(lst)
