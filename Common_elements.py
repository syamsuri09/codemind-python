m,n = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
a1=[]
for i in a:
    if(i not in a1):
        a1.append(i)
        
b1=[]
for i in b:
    if i not in b1:
        b1.append(i)
c = []
for i in a1:
    if i in b1:
        c.append(i)
print(*c)