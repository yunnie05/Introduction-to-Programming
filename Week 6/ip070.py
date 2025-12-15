def possible_sums(coins):
    coins= list(coins)
    s= set()
    for f in coins: #fixa um coin
        s.add(f)
        for i in coins:
            s.add(f+i)
            temp= f+i
            for k in coins:
                s.add(k+temp)
    return s

def possible_sums2(coins,sum):
    #ans= []
    if len(coins)==0:
        if sum!=0:
          return [sum]
        else:
            return coins[0]
    l0= possible_sums2(coins[1:],sum+coins[0])
    l1= possible_sums2(coins[1:],sum)
    return l0+l1
    
print(possible_sums2([2,3],0))