def swap_list(lst):
    n= len(lst)
    if n%2!=0:
        n-=1
    for i in range(0,n,2):
        (lst[i],lst[i+1])=(lst[i+1],lst[i])