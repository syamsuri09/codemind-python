m,n = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

a = list(set(a))
b = list(set(b))

c = 0
for i in a:
    if i not in  b:
        c+=1
for j in b:
    if j not in a:
        c+=1
print(c)