n = int(input())
ar = list(map(int,input().split()))

e = 0
for i in range(0,n):
    if i % 2 == 0:
        e += ar[i]
print(e)