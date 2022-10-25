n = int(input())
arr = list(map(int,input().split()))

c= 0
for i in range(len(arr)):
    t = arr[i]
    t = str(t)
    if t[::-1] == t:
        c +=1
print(c)
