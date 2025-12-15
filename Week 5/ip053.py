def occurrences(lst,x):
    res= []
    for i in range(len(lst)):
        if lst[i]==x:
            res.append(i)
    return res