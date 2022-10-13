n = int(input())
l = list(map(int,input().split()))

count = 0
for i in l:
    count+=i
total = count // len(l)
sum = 0
for i in l:
    if i >= total:
        sum +=1
print(sum)