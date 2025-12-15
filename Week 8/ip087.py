def weekends(k,planets):
    return weekends_rec(k,planets,[])

def weekends_rec(k,planets,cur):
    ans= []
    if len(cur)==k:
        return [cur]
    for i in planets:
       ans.extend(weekends_rec(k,planets,cur+[i]))
    return ans