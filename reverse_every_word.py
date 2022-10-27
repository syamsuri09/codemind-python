n = list(map(str,input().split()))

c =[]
for i in n:
    t = i[::-1]
    c.append(t)
print(*c)