m,n = map(int,input().split())
arr = list(map(int,input().split()))

c = 0
for i in arr:
    if i % n == 0:
        c+=1
print(abs(len(arr)-c))