n = int(input())
arr = list(map(int,input().split()))
x,y = map(int,input().split())
b = []

for i in arr:
    if x <= i and y >= i:
        b.append(i)
if len(b) == 0:
    print("-1")
else:
    print(*b)