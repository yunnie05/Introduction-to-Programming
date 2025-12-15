def sum_all_odds(a,b): #somar ímpares
    soma= 0
    y=1
    if b < a:
        temp= a
        a= b
        b= temp
    if a % 2!=0: #se a for impar, a soma é de 2 em 2
        if b<0:
            y = -y
        for i in range(a,b+1,2):
            soma += i
        return soma    
    for i in range(a+1,b+1,2): #se a for par soma 1 faz de 2 em 2
        soma += i
    return soma


