a = int(input())
b = int(input())

for i in range(a,b+1):
    i = str(i)
    c = 0
    for j in i:
        if int(j) != 0:
            if int(i) % int(j) == 0:
                c+=1
    if len(i) == c:
        print(i,end=" ")