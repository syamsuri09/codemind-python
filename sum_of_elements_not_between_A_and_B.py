n = int(input())
l = list(map(int,input().split()))
a,b = map(int,input().split())

total = []
for i in range(len(l)):
    if l[i] < a or l[i]>b :
        total.append(l[i])
print(sum(total))