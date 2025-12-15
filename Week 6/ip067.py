#perceber que item do menu tem o preço mais alto
def highest_items(menu):
    high= list(menu.values())
    high.sort()
    high= int(high[-1])
    lst=[]
    for i in menu:
        if menu[i]==high:
            lst.append(i)
    return lst