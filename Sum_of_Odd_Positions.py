n = int(input())
ar = list(map(int,input().split()))

o = 0
for i in range(0,n):
    if i % 2 == 1:
        o += ar[i]
print(o)