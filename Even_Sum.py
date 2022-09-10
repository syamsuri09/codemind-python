n = int(input())
ar = list(map(int,input().split()))

o = 0
for i in ar:
    if i % 2 == 0:
        o += i
print(o)