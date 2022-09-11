n = int(input()) 
ar = list(map(int,input().split()))

for i in ar:
    if i % 2 == 0:
        a = ar.index(i)
        index = ar[a]
print(index)