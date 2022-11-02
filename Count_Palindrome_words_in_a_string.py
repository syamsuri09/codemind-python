m = input().lower()
m = m.split()

c = 0
for i in range(len(m)):
    p = m[i][::-1]
    if m[i] == p :
        c+=1
print(c)