n = input()
n = n.lower()
c = []
for i in n:
    if i not in c and i != " ":
        c.append(i)
l = sorted(c)
d =''
for j in l:
    d +=j
print(d)