m = int(input())
n = int(input())

x = m+n+1

while x :
    s = 0
    for i in range(2,x):
        if x % i == 0:
            s = 1
            x +=1
            break
    if s == 0:
        print(x-(m+n))
        break