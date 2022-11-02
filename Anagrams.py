m = input().lower()
n = input().lower()

c = []
for i in m:
    if i not in n:
        c.append(i)
if len(c) == 0:
    print(True)
else:
    print(False)