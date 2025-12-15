def swap(word):
    word= list(word)
    n= len(word)
    res= ""
    if n % 2 != 0:
        n = n - 1
        temp= word[n]
    for i in range(0,n,2):
        (word[i],word[i+1])=(word[i+1],word[i])
        #temp= word[i]
        #word[i]=word[i+1]
        res+= word[i]
       # word[i+1]=temp
        res+= word[i+1]
    if word[len(word)-1]!=temp:
        word.append(temp)
    return res


print(swap("programming"))
