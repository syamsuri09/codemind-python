n = int(input())
arr = list(map(int,input().split()))
x = int(input())
b = 0

for i in arr:
    if x >= i :
        b+=i
print(b)