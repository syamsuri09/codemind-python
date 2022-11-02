m,n = list(map(int,input().split()))

even = 0
odd = 0
for i in range(1,m+1):
    a = list(map(int,input().split()))
    for j in a:
        if j % 2 == 0:
            even += j
        else:
            odd += j
print(even,odd)