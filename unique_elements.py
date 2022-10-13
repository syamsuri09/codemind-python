n = int(input())
l = list(map(int,input().split()))

b = []
for i in l:
    if (i not in b ):
        b.append(i)
for j in b:
    print(j,end = " ")