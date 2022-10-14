n = int(input())
l = list(map(int,input().split()))
k = int(input())
x = list(set(l))

b = []
for i in x:
    c = 0
    for j in l:
        if i == j:
            c+=1
    if c == k:
        b.append(i)
if len(b) == 0:
    print("-1")
else:
    for z in b:
        print(z,end= " ")