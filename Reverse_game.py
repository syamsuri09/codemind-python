n = int(input())
arr = list(map(int,input().split()))

c= []
for i in range(len(arr)):
    t = arr[i]
    t = str(t)
    p = t[::-1]
    p = int(p)
    c.append(p)
print(*c)