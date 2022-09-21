x,y = map(int,input().split())

for i in range(1,y+1):
    if i % 2 == 1:
        mul = x * i
        print(x, "x", i, "=", mul  )