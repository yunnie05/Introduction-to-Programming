def swap(menu):
    new= {}
    for (key,values) in menu.items():
        new[values]= key
    return new