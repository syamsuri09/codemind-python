n = int(input())
ar = list(map(int,input().split()))
s=sum(ar)
avg=int(s/len(ar))
if avg in ar:
    print("True")
else:
    print("False")