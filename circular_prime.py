n = int(input())

first = True
for i in range(2,n):
    if n % i == 0:
        first = False
if first == True and i != 1:
    s = str(n)[::-1]
    s = int(s)
    x = 1
    for i in range(2,s):
        if s % i == 0:
            x = 0
            break
    if x == 1:
        print("circular prime")
    else:
        print("prime but not a circular prime")
else:
    print("not prime")