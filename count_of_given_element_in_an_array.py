n = int(input())
ar = list(map(int,input().split()))
z = int(input())

k = 0
for i in ar:
    if z == i:
        k +=1
print(k)