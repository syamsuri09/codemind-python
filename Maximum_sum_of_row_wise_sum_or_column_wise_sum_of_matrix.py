m,n = list(map(int,input().split()))

c = []
for i in range(1,m+1):
    a = list(map(int,input().split()))
    total = sum(a)
    c.append(total)
print(max(c))