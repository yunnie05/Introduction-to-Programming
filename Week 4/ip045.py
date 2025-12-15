#needle in haystack
def substring(needle, haystack): 
    for i in needle:
        if len(haystack)==0:
            return False
        for j in range(len(haystack)):
            if i==haystack[j]:
                res= True
                break  
            else:
                res= False
        haystack= haystack[j+1::]
        if not res:
            break
    return res