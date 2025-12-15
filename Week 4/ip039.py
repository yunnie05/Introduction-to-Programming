def duplicate(tup):
    res= ()
    for i in tup:
        res+= (i,i) #ou res+= (i,)*2
    return res

