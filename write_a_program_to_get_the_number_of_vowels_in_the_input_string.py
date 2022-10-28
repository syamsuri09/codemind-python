n = input()
upper = ["A","E","I","O","U"]
lower = ["a","e","i","o","u"]

c = 0
for i in n:
    if i in upper:
        c +=1
c1 = 0
for j in n:
    if j in lower:
        c1+=1
total = c + c1
if total == 0:
    print("0")
else:
    print(total)