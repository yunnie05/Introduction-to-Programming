
def evolve(initial, n):
    for i in range(n+1):
        new=""
        print(initial)
        for j in initial:
            if j== "A":
                new +='AB'
            elif j== 'B':
                new += 'A'
        initial= new