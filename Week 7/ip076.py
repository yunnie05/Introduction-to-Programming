def find_all(keyword, text):
    i= 0
    pos= []
    while(text.find(keyword,i)!=-1):
       x= text.find(keyword,i)
       pos.append(x)
       i=x+1
    return pos