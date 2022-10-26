n = int(input())
arr = list(map(int,input().split()))
s=0
for i in arr:
    su=0
    while i:
        su+=i%10
        i//=10
    s+=su
print(s)