#retorna o nº de elementos em que está contida   
def find_el(n):
    fp= 1
    fs= 2
    s= fs
    if n==1 or n==2:
        return n
    while fs < n:
        s= fs
        new_line= fp+ fs
        (fp,fs)=(fs,new_line)
    return s

def whichone(n):
    base= {1: 'A', 2: 'B'}
    s= find_el(n)
    if s <= 2 and n<=s:
        return base[s]
    if n > s:
        n= n-s
    return whichone(n)