n = input()
upper = ["A","E","I","O","U"]
lower = ["a","e","i","o","u"]

lis = []
for i in lower:
    if i not in n:
        lis.append(i)
li = []
for j in lower:
    if j not in n:
        li.append(j)
if len(lis) == 0 or len(li)==0:
    print("True")
else:
    print("False")