m = int(input())
n = int(input())

for i in range(m,n+1):
    s = True
    for j in range(2,i):
        if i% j == 0:
            s = False 
    if s == True and i !=1:
        print(i)