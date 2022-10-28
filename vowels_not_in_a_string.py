n = input()
c = ["a","e","i","o","u"]

l = []
for i in c:
    if i not in n:
        l.append(i)
if len(l) == 0:
    print("0")
else:
    print(*l)