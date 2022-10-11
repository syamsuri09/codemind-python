n = int(input())
ar = [0,1]

for i in range(n-2):
    val =  ar[-1] + ar[-2]
    ar.append(val)
for i in ar:
    print(i,end=" ")