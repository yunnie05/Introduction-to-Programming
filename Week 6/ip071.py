def frequency(ingredients):
    it= list(set(ingredients))
    it.sort()
    ingredients.sort()
    res= {}
    for i in it:
        count= 0
        for j in ingredients:
            if j==i:
                count+=1
            else:
                break
        ingredients= ingredients[count:]
        res[i]= count
    return res
