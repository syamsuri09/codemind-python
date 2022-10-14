n = int(input())
l = list(map(int,input().split()))

c = 0
count = 0
for i in l:
    s = True
    for j in range(2,i):
        if i % j == 0:
            s = False
            break
    if s == True and i > 1:
        c+=i
        count+=1 
total = c / count
print("%.2f" % total)