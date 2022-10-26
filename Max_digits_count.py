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
maximum = min(c)
e = 0
for j in d:
    j = abs(j)
    j = str(j)
    if len(j) == max(c):
        e+=1
print(e)