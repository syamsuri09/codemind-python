a = int(input())

for j in range(a):
    n = int(input())
    b = []
    while n:
        p = n% 2
        n = n // 2
        b.append(p)
    for i in b[::-1]:
        print(i,end = "")
    print()