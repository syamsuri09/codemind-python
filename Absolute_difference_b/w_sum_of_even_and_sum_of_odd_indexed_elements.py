n = int(input())
ar = list(map(int,input().split()))
e=0
o=0
for i in range(0,n):
    if i%2==0:
        e+=ar[i]
    else:
        o+=ar[i]
if e>o:
    print(e-o)
else:
    print(o-e)