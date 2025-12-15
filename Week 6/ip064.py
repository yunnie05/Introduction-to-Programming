def rename(menu, old_name, new_name):
    for i in menu:
        if i==old_name:
            val= menu[i]
            menu[new_name]= val
            del menu[i]
            break
    return None