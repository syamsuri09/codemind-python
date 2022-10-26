n = int(input())
arr = list(map(int,input().split()))
d=[]
for i in arr:
    if(i not in d):
        d.append(i)
c=[]
for i in d:
    i=abs(i)
    b=str(i)
    c.append(len(b))
q=max(c)
for i in d:
    if(i<0):
        b=str(-i)
        b=len(b)
        if(b==q):
            print(i,end=" ")
    else:
        b=str(i)
        if(len(b)==q):
            print(i,end=" ")
        