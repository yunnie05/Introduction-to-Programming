def sum(a,b):
    matrix= []
    soma_l= []
    if (len(a)!=len(b) or len(a[0])!=len(b[0])):
        return None
    lin= len(a)
    col= len(a[0])
    for i in range(lin):
        for j in range(col):
            soma_l.append(a[i][j]+b[i][j])
        matrix.append(soma_l)
        soma_l= []
    return matrix