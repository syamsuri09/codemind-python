n = int(input())
l = list(map(int,input().split()))

b = []
for i in l:
    if i % 2 == 0:
        b.append(i)
if len(b) == n:
    print("True")
else:
    print("False")