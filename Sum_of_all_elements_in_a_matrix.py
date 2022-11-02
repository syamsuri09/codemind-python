m,n = list(map(int,input().split()))

total = 0
for i in range(1,m+1):
    a = list(map(int,input().split()))
    total += sum(a)
print(total)