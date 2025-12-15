def process_data(lst):
    sum= []
    for i in range(len(lst)-1):
        try:
            a= int(lst[i])
            b= int(lst[i+1])
            sum.append(a+b)
        except (ValueError,TypeError):
            continue
    return sum