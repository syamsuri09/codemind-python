n = int(input()) 
ar = list(map(int,input().split()))

for i in ar:
    if i % 2 == 1:
        a = ar.index(i)
        index = ar[a]
print(index)