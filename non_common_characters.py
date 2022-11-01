m = input()
m = m.lower()
n = input()
n = n.lower()

def two_strings(a):
    s = ""
    for i in a:
        if i !=" ":
            s+=i
    return s

a = two_strings(m)
b = two_strings(n)

li = []
for j in b:
    if j not in a:
        li.append(j)
for z in a:
    if z not in b:
        li.append(z)
l = sorted(li)
c = []
for i in l:
    if i not in c:
        c.append(i)
s = ''
for x in c:
    s+=x
print(s)