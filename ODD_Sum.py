n = int(input())
ar = list(map(int,input().split()))

o = 0
for i in ar:
    if i % 2 == 1:
        o += i
print(o)