n = int(input())
arr = list(map(int,input().split()))

c = ""
for i in arr:
    i = str(i)
    c +=i
d = 0
for j in c:
    d +=int(j)
print(d)