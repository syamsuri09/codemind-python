n = int(input())

for i in range(n):
    mul = 1
    n = int(input())
    for i in range(1,n+1):
        mul *= i
    print(mul)