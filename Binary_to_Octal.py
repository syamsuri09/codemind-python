z = int(input())

for i in range(z):
    a = input()
    a = a[::-1]
    
    d = []
    for i in range(len(a)):
        b = 2 ** i
        c = int(a[i]) * b
        d.append(c)
    s = (sum(d))
    n = s
    b = []
    while n:
        p = n% 8
        n = n // 8
        b.append(p)
    for i in b[::-1]:
        print(i,end="")
    print()