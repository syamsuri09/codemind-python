n = int(input())
l = list(map(int,input().split()))
x = int(input())

c = 0
for i in l:
    s = True
    for j in range(2,i):
        if i % j == 0:
            s = False
            break
    if s == True and i > 1:
        if x >= i:
            c += 1
print(c)