n = int(input())
l = list(map(int,input().split()))

x = list(set(l))
b = []
count=0
for i in x:
    c = 0
    for j in l:
        if i == j: 
            c+=1
    if c == i:
        b.append(i)
if len(b) == 0:
    print("-1")
else:
    print(min(b),max(b),end=" ")