n= int(input())
BASIS_P= 50.0
total= 0.00
for i in range(1,n+1):
    price= BASIS_P/i
    print(f"Night {i}: {round(price,2)}E")
    total += price
print(f"Total: {round(total,2)}E")