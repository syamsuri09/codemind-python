n = int(input())
ar = [0,1]

for i in range(n):
    val =  ar[-1] + ar[-2]
    ar.append(val)
    if val == n:
        print("True")
        break
else:
    print("False")