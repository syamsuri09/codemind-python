m = input().lower()
m = m.split()


for i in range(len(m)):
    p = m[i][::-1]
    if m[i] == p :
        print(True)
    else:
        print(False)