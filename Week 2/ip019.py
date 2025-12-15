import math

radius_1= float(input())
x_1= float(input())
y_1= float(input())
radius_2= float(input())
x_2= float(input())
y_2= float(input())

area_2= math.pi* radius_2**2
dist= math.sqrt((x_1-x_2)**2+(y_1-y_2)**2)
print(dist,radius_2-radius_1,radius_1-radius_2)
sum_r= radius_1+radius_2
diam_1= 2*radius_1
diam_2= 2*radius_2
if (dist==sum_r) :
   print("The circles are tangent.")
elif(dist == radius_1-radius_2) or (dist== radius_2-radius_1):
    print("The circles are tangent.")
else:
    print("The circles are not tangent.")