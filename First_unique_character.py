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
if len(d) == 0:
    print('-1')
else:
    print(d[0])