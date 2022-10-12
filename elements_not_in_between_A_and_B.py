n = int(input())
l = list(map(int,input().split()))
a,b = map(int,input().split())

total = []
for i in range(len(l)):
    if l[i] < a or l[i]>b :
        total.append(l[i])
        
if len(total) > 0:
    for i in total:
        print(i,end=" ")
else:
    print("-1")