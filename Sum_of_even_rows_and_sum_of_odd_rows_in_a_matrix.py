m,n = list(map(int,input().split()))

even = 0
odd = 0
for i in range(1,m+1):
    if i % 2 != 0:
        a = list(map(int,input().split()))
        odd += sum(a)
    else:
        a = list(map(int,input().split()))
        even += sum(a)
print(odd,even)