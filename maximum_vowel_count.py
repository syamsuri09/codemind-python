n = list(map(str,input().split()))
upper = ["A","E","I","O","U"]
lower = ["a","e","i","o","u"]

l = []
for i in range(len(n)):
    c = 0
    for j in n[i]:
        if j in lower:
            c+=1
    l.append(c)
    c = 0
print(max(l))