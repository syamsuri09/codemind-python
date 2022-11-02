m = input().lower()

c = []
for i in m:
    if i not in c:
        c.append(i)
if len(c) == len(m):
    print(True)
else:
    print(False)