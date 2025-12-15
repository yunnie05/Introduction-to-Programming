start_hr= int(input())
start_min= int(input())
start_seg= int(input())
baking_hr= int(input())
baking_min= int(input())
baking_seg= int(input())
fin_seg= start_seg + baking_seg
fin_min= start_min + baking_min
fin_hr= start_hr + baking_hr

total_fin= fin_seg + (fin_min*60) + (fin_hr * 3600)
fin_hr= (total_fin // 3600) % 24
total_fin= (total_fin % 3600)
fin_min= (total_fin // 60) % 60
fin_seg= total_fin % 60
print(f"Take the cake out at {fin_hr:02}:{fin_min:02}:{fin_seg:02}.")