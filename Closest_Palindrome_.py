a = int(input())

m = a + 1
while 1:
    u = str(m)
    v = u[::-1]
    if int(m) == int(v):
        break
    else:
        m += 1
        
n = a -1
while 1:
    x = str(n)
    y = x[::-1]
    if int(n) == int(y):
        break
    else:
        n -= 1
        
if abs(int(m) - a) < abs(int(n) - a):
    print(int(m))
elif abs(int(m) - a) == abs(int(n) - a):
    print(int(n),int(m))
else:
    print(int(n))