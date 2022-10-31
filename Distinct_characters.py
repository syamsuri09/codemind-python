n = input()
n = n.lower()
c = ''
for i in n:
    if i != " ":
        c+=i
d = ''
for j in c:
    if (c.count(j)==1):
        d+=j
e = ''
l = sorted(d)
for z in l:
    e+=z
print(e)