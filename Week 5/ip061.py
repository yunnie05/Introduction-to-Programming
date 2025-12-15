def spiral_path(m):
    ans= []
    rows,cols= len(m), len(m[0])
    incy= [0,1,0-1]
    incx= [1,0,-1,0]
    x,y,dir= 0,0,0
    for i in range(0, rows*cols):
        ans.append(m[y][x])
        m[y][x]= None
        y,x= y+incy[dir], x+incx[dir]
        if  y<0 or y>=rows or x<0 or x>=cols or m[y][x]==None:
            y,x= y-incy[dir], x-incx[dir]
            dir= (dir+1) % 4
            y,x= y+incy[dir], x+incx[dir]
    return ans