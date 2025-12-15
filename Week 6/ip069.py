def remove(x, menu):
    r= {i for i in menu if x==i[0]}
    menu -=r
