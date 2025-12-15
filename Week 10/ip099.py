def future_exceptions(f,a,b):
    count=0
    for i in range(a,b+1):
        try:
            f(i)
        except:
            count+=1
    return count