n = list(map(str,input().split()))

for i in range(len(n)):
    if i % 2 == 0:
        t = n[i]
        p = t[::-1]
        print(p,end=" ")
    else:
        print(n[i],end=" ")