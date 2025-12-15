import math
opt= input()
radius= float(input())
if opt=="1":
    print(f"Diameter: {round(radius*2,2)}")
elif opt=="2":
    print(f"Perimeter: {round(2*radius*math.pi,2)}")
elif opt=="3":
    print(f"Area: {round(math.pi*radius**2,2)}")
else:
    print("Invalid Option.")    