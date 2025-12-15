def super_swap(menu):
    ls= set()
    res= {}
    v= set(menu.values())
    for i in v:
        for (x,y) in menu.items():
            if y==i:
                ls.add(x)
        res[i]=ls.copy()
        ls.clear()
    return res
