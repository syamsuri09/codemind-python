a,b = map(int,input().split())

c = a + 1
d = b + 1

if c == b:
    print("Yes")
elif d == a:
    print("Yes")
elif a == 10 and b == 1 or a == 1 and b == 10:
    print("Yes")
else:
    print("No")