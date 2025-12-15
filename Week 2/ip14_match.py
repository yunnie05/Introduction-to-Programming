import math

n= int(input())
radius= float(input())
match(n):
    case 1:
        print(f"Diameter: {round(2*radius,2)}")
    case 2:
        print(f"Perimeter: {round(math.pi*2*radius,2)}")
    case 3:
        print(f"Area: {round(math.pi*radius**(1/2),2)},2)")
    case _:
        print("Invalid Option.")
        
