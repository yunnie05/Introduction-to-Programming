d= float(input())
hr= int(input())
min= int(input())
conv_min= hr* 60
total_min= conv_min + min
km_hr= (60*d)/total_min
print(int(round(km_hr,0)))