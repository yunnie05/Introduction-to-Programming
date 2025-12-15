#se eu não conseguir converter para int dá ValueError
#se for 0 dá o erro típico
'''def transform(lst):
    new= []
    for l in lst:
        temp= []
        if len(l)==0:
            del lst[lst.index(l)]
        for col in l:
            try:
                col= 1/int(col)
                temp.append(col)
            except Exception as error:
                print(f'Error: {type(error).__name__} for value "{col}": {error}.')
        if len(temp)!=0:
            new.append(temp)
    return new'''
    
def transform(lst): 
    new= []
    for l in lst:
        temp= []
        if len(l)==0:
            continue
        for col in l:
            try:
                col= 1/col
                temp.append(col)
            except Exception as error:
                if type(error).__name__ == "TypeError":
                    try:
                       col= 1/int(col)
                       temp.append(col)
                    except Exception as error:
                        print(f'Error: {type(error).__name__} for value "{col}": {error}.')
                else:
                    print(f'Error: {type(error).__name__} for value "{col}": {error}.')
        if len(temp)!=0:
            new.append(temp)
    return new

print(transform([[2, 8, 4], ["abc", "def", "ghi"], [1, 5, 10]]))
