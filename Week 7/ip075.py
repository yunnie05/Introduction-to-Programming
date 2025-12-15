def word_types(lst):
    low= 0
    upp= 0
    other = 0
    for c in lst:
        if c.islower():
            low+=1
        elif c.isupper():
            upp += 1
        else:
            other+=1
    return (low,upp,other)