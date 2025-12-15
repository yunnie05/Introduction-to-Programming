def sum_integers(data):
    if isinstance(data, int):
        return data
    elif isinstance(data,float) or isinstance(data,str) or len(data)==0:
        return 0
    return sum_integers(data[0]) + sum_integers(data[1:])
