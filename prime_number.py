n = int(input())

f = True
for i in range(2,n):
    if n % i == 0:
        f = False
if f == True:
    print("prime")
else:
    print("not a prime")