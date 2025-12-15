def rotate(lst, dir):
    n= len(lst)
    if n!=0:
      if dir == "right":
        x= lst[n-1]
        lst.pop(n-1)
        lst.insert(0,x)
      elif dir == "left":
        x= lst[0]
        lst.pop(0)
        lst.append(x)
    return None