n = input()

count = 0
total = 0
for i in n:
    count+=1
    mul = int(i) ** count
    total += mul
if int(n) == total:
    print("True")
else:
    print("False")