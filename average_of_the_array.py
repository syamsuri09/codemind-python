n = int(input())
ar = list(map(int,input().split()))

k = 0
for i in ar:
    k += int(i)
x = k/n
print("%.2f" % x)