n = list(map(str,input().split()))
lower = ["a","e","i","o","u"]
l = []
for i in range(len(n)):
    c = 0
    for j in n[i]:
        if j in lower:
            c+=1
    l.append(c)
t = min(l)
c = 0
for i in l:
    if t == i:
        c +=1
print(c)