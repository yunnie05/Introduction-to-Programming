'''def nested_exceptions2(tree):
    new= []
    for i in tree:
        if isinstance(i, tuple):
            aux= ()
            for k in i:
                aux += (ver(k),)
            new.append(aux)
        else:
            new.append(ver(i))
    return tuple(new)'''

def ver(el):
    try:
        test= el()
    except Exception as error:
        return True
    else:
            return False
        
        
def nested_exceptions(tree):
    new= []
    for i in tree:
        if isinstance(i, tuple):
            aux= nested_exceptions(i)
            new.append(aux)
        else:
            new.append(ver(i))
    return tuple(new)

