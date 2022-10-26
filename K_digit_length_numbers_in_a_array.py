m,n = map(int,input().split())
arr = list(map(int,input().split()))

b = arr

c = 0
for i in b:
    if i<0:
        i = str(-i)
        if n == len(i):
            c+=1
    else:
        i = str(i)
        if len(i) == n:
            c+=1
print(c)