n = list(map(str,input().split()))

first = n[0]
last = n[-1]

c = []
d = []
for i in first:
    char = ord(i)
    c.append(char)
for j in last:
    char1 = ord(j)
    d.append(char1)
s = min(c) 
t = max(d)
print(chr(s),chr(t))