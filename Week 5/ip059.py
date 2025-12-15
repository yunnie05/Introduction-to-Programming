
def rev(lst):
    tmp= []
    t= []
    for (x,y) in lst:
        t= []
        for (f,g) in lst:
            if f==x:
                t.append(g)
        if t not in tmp:
            tmp.append(t)
    tmp.reverse()
    lst= []
    for i in tmp:
        lst.extend(i)
    return lst
        

def sort_strings(lst):
    tmp= [(len(x),x) for x in lst]
    tmp.sort()
    lst.clear()
    lst.extend(rev(tmp))
    