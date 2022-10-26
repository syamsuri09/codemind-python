n = int(input())
arr = list(map(int,input().split()))
d = []
for j in arr:
    if j not in d:
        d.append(j)
c = []
for i in d:
    i = abs(i)
    t = len(str(i))
    c.append(t)
e = 0
for j in d:
    j = abs(j)
    j = str(j)
    if len(j) == min(c):
        e+=1
print(e)