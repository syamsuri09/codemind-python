a,b = map(int,input().split())

while a != 0 and b != 0:
    if a > b:
        a %= b
    else:
        b %= a
gcd = a if b == 0 else b
print(gcd)