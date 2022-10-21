n = int(input())
arr = list(map(int,input().split()))

a = arr[:len(arr)//2]
b = arr[len(arr)//2:]

x = sum(a)
y = sum(b)
print(x)
print(y)