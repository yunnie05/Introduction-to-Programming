'''def quantities(coins):
    p_sums = [0]
    for coin in coins:
        new_sums = [existing_sum + coin for existing_sum in p_sums]
        p_sums.extend(new_sums)
    return set(p_sums)
    '''

def quantities(coins):
    if len(coins)==0:
        return {0}
    rest = quantities(coins[1:])
    new_sums = {x+coins[0] for x in rest}
    return rest.union(new_sums)