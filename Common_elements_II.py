m,n = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))


c = []
for i in a:
    if i not in b:
        c.append(i)
for j in b:
    if j not in a:
        c.append(j)
print(*c)