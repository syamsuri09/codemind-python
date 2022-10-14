x = int(input())
for z in range(x):
    n = input()
    n=n[::-1]
    
    c = 0
    for i in range(len(n)):
        a = 8 ** i
        b = int(n[i]) * a
        c += b
    n = c
    b = []
    while n:
        p = n% 2
        n = n // 2
        b.append(p)
    for i in b[::-1]:
        print(i,end="")
    print()