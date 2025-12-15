def middle(lst):
    n= len(lst)
    lst.sort()
    if n%2==0:
        return lst[n//2-1:(n//2)+1]
    else:
       return [lst[n//2]] 