n = int(input())

add = 0
for i in str(n):
    mul = 1
    for i in range(1,int(i)+1):
        mul *= i
    add += mul
if int(n) == add :
    print("The number", n, "is a strong number")
else:
    print("The number", n, "is not a strong number")