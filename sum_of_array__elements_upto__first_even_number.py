n = int(input())
arr = list(map(int,input().split()))

b=[]
for i in arr:
    if i % 2 == 0:
        break
    b.append(i)
print(sum(b))