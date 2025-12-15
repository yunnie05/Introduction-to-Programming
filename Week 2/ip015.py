price= float(input())
c= input()
if c== "P":
    price += price*0.06
    print(f"Customer: {c} | Price: {round(price,3)}")
elif c== "F":
    if price > 200:
        price -= price*0.10
    elif price >= 50:
        price -= price*0.05
    else:    
        price-= price*0.02
    print(f"Customer: {c} | Price: {round(price,3)}")