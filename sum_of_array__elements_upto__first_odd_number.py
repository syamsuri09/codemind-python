n = int(input())
arr = list(map(int,input().split()))

b=[]
for i in arr:
    if i % 2 == 1:
        break
    b.append(i)
print(sum(b))