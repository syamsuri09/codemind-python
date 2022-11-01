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
    if j in a:
        li.append(j)
for z in a:
    if z in b:
        li.append(z)
l = sorted(li)
c = ''   
for x in l:
    if x not in c:
        c+=x
if len(c)==0:
    print("-1")
else:
    print(c)