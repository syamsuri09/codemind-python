n = int(input())
l = list(map(int,input().split()))

count = 0
for i in range(1,n-1):
    if(l[i+1]%2==0) and (l[i-1]%2==0):
        odd = l[i]
        for i in str(odd):
            if int(i)%2==0:
                count += 1
print(count)