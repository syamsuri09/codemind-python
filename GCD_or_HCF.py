a,b = map(int,input().split())
while a < b:
    a,b = b,a
c = a
while True:
    if a%c == 0 and b%c == 0:
        print(c)
        break
    c -=1