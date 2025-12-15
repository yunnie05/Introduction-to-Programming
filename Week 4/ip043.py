def search(tup, value):
    first= len(tup)-1
    last= -1
    for i in range(len(tup)):
        if value==tup[i]:
            if i < first:
                first= i
            if i > last:
                last= i
    if tup[first]==value and tup[last]!=value:
       last= first
    elif tup[first]!=value:
        first= -1
    return (first,last)
