m = input().lower()
m = m.split()
n = input().lower()
n = n.split()

for i in n:
    if i in m:
        print(i,end=" ")