grade= float(input())
if grade < 0:
    print("NA")
elif grade >= 90:
    print(5)
elif grade >= 70:
    print(4)
elif grade >= 50:
    print(3)
elif grade >= 20:
    print(2)
else:
    print(1)