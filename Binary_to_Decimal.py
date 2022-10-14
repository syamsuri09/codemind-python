a = int(input())

for i in range(a):
    n = input()
    n = n[::-1]
    
    c = 0
    for i in range(len(n)):
        a = 2 ** i
        if n[i] == "1":
            c+=a
    print(c)