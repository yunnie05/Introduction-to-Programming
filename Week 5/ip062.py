def spiral_number(y,x):
    if x>=y:
        if x%2==1: return x*x - (y-1)
        else: return (x-1)*(x-1) + y
    else:
        if y%2==0: return y*y - (x-1)
        else: return (y-1)*(y-1) + x