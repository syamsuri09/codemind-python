n = int(input())
ar = list(map(int,input().split()))

l = []
for i in ar:
    if int(i) % 2 == 0:
        l.append(i)
for i in ar:
    if int(i) % 2 == 1:
        l.append(i)
for i in l:
    print(i, end = " ")