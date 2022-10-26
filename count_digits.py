n = int(input())
arr = list(map(int,input().split()))

for i in arr:
    i = abs(i)
    t = str(i)
    print(len(t),end=" ")
