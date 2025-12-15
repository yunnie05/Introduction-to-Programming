def extract_initials(text):
    res= ""
    text= text.split()
    for i in text:
        res+= i[0].lower()
    return res        
    

def sort_initials(text):
    u= []
    text= (text.lower()).title()
    aux= extract_initials(text)
    for i in set(aux):
        s= aux.count(i)
        u += [(s,i)]
    u.sort()
    u.reverse()
    s= sw(u)
    return s
        
def to_string(lst):
    ans= ""
    for i in lst:
        ans += i
    return ans

def sw(text):
    ans= ""
    j= 0
    for i in range(len(text)):
        i= j
        if (i>=len(text)):
                break
        num= text[i][0]
        aux = []
        j= i
        while(text[j][0]==num):
            aux.append(text[j][1])
            j+=1
            if (j>=len(text)):
                break
        aux.sort()
        ans += to_string(aux)
    return ans
            
                        
           
        
attack_points = 100
health_points = 20
print(attack_points != 0 and health_points >=50)