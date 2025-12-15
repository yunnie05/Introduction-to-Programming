def unique(lst):
    res=[]
    for i in lst:
        n=lst.index(i)
        if i not in lst[n+1::]:
            res.append(i)
    return res