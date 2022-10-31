n = input()
n = n.lower()
c = ''
for i in n:
    if i != " ":
        c+=i
d = 0
for j in c:
    if (c.count(j)==1):
        d+=1
print(d)