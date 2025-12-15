#a e b são os tamanhos
#k é o número de 1's

def binary(a,b,k):
    return binary_rec(a,b,k,"")

def binary_rec(a,b,k,cur):
    if len(cur)==b:
        return[cur]
    ans= []
    if len(cur)==a:
        ans+= [cur]
        a+=1
    ans += binary_rec(a,b,k,cur+"0")
    if k>0:
        ans+= binary_rec(a,b,k-1,cur+"1")
    return list(set(ans))



'''def binary(a,b,k):
  return binary_rec(a,b,k,"")
  
def binary_rec(a,b,k,cur):
#def binary_rec(a,b,k,cur, min_cur_len, max_cur_len):
    if b==0: 
        return [cur]
    ans= []
    if a>=0: 
        ans+= [cur]
    ans += binary_rec(a-1,b-1,k,cur + "0")
    if k>0:
        ans += binary_rec(a-1,b-1,k-1, cur + "1")
    return ans
    '''

