n = int(input())

for i in range(1,n+1):
    s = i ** 2
    if s == n:
        print("True")
        break
else:
    print("False")