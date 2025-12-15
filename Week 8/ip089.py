def rem(planets, p):
    new= []
    for i in planets:
        if i!=p:
            new.append(i)
    return new

'''def visit(planets):
    return visit_rec(planets,[])

def visit_rec(planets,fir):
    ans=[]
    if len(planets)==0:
        if len(fir)==0:
            return []
        return [fir]
    for i in planets:
        aux= rem(planets,i)
        ans.append(i)
        if fir in planets:
            fir= i
        else:
            fir= ""
        ans+= visit_rec(aux,fir)
    return ans'''
        

def visit_rec(planets,ans):
    new= []
    res= []
    temp= []
    temp= ans.copy()
    #caso base
    if len(planets)==0:
        temp.append(temp[0])
        return temp
    #caso recursivo
    #print(planets)
    for i in planets:
        aux= rem(planets,i)
        ans.append(i)
        res= visit_rec(aux,ans)
        if isinstance(res[0],list):
            new.extend(res)
        elif not isinstance(res[0],list):
            new.append(res)
        ans.clear()
        ans.extend(temp)
        res= []
    return new

def visit(planets):
    return visit_rec(planets,[])
