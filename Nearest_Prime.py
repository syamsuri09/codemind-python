n = int(input())

for i in range(n):
    a = int(input())
    x1 = a 
    while a:
        s1 = 0
        for i in range(2,x1):
            if x1 % i == 0:
                s1 = 1
                x1 += 1
                break
        if s1 == 0:
            x1
            break
    x2 = a 
    while a:
        s2 = 0
        for j in range(2,x2):
            if x2 % j == 0:
                s2 = 1
                x2 -= 1
                break
        if s2 == 0:
            x2
            break
    if abs(x2-a) > (x1-a):
        print(x1)
    else:
        print(x2)