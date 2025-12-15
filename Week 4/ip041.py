def extremes(words):
    a= len(words[0])
    b= len(words[0])
    for i in words:
        if len(i) < a:
            a= len(i)
        elif len(i) > b:
            b= len(i)
    return (a,b)