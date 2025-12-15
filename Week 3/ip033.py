def largest_sequence(num):
    num= str(num)
    length = 0
    count= 1
    for i in range(1,len(num)):
        if int(num[i]) <= int(num[i-1]):
            if count > length:
                length= count
                count=1
                continue
            count=1
            continue
        count+=1 
    if count>length:
        return count    
    return length

#conta os elementos e para quando i+1 < i

