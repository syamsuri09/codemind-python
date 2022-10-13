n = int(input())
l = list(map(int,input().split()))
a,b = map(int,input().split())

h = []
for i in range(len(l)):
    if l[i] < a or l[i] > b:
        h.append(l[i])
if len(h) == 0:
    print("-1")
else:
    print(max(h))