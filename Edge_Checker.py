a,b = map(int,input().split())

c = a + 1
d = a - 1
if c == b:
    print("Yes")
elif c == 11 and b == 1:
    print("Yes")
elif a == 1 and b == 10:
    print("Yes")
elif d == b:
    print("Yes")
else:
    print("No")