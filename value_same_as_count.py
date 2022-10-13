n = int(input())
l = list(map(int,input().split()))

x = list(set(l))

count=0
for i in x:
    c = 0
    for j in l:
        if i == j:
            c+=1
    if c == i:
        count += 1
print(count)