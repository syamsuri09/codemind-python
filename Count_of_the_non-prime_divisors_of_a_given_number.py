n = int(input())
count = 0
for i in range(1,n+1):
    if n % i == 0:
        s = 0
        #print(i)
        for j in range(2,i):
            if i % j == 0:
                s = 1
                break
        if s == 1:
            count+=1
print(count+1)