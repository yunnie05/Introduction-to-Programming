def list_to_matrix(lst,r,c):
    res= []
    a= 0
    for i in range(r):
        res.append(lst[a:a+c])
        a+= c
    return res