def calculator(a,b,c):
    soma=a + b +c
    Max= a
    min= a
    if b > Max:
        Max= b
    if c > Max:
        Max= c
    if b < min:
        min= b
    if c < min:
        min= c
    msg = str(Max) + " " + str(min) + " " + str(soma)
    return msg

print(calculator(45, 12, 36))