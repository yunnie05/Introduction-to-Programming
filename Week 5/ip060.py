def eeny_meeny(lst,k):
    k-= 1
    new= []
    while(len(lst)>0):
        comp= len(lst)
        pos= k % comp
        new.append(lst[pos])
        if pos==comp-1 or pos==0:
            del lst[pos]
        else:
            lst= lst[pos+1:] + lst[:pos]
    return new