n = int(input())

for i in range(n):
    t = i*(i+1)
    if n == t:
        print("YES")
        break
else:
    print("NO")