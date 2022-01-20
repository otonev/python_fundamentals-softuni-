n=float(input())
if abs(n) < 1 and n != 0:
    print("small",end=" ")
elif 1000000 < abs(n):
    print("large",end=" ")
if n > 0:
    print("positive")
elif n < 0:
    print("negative")
else:
    print("zero")