x = input()

add = 0
mul = 1
for i in x:
    add += int(i)
    mul *= int(i)
if add == mul:
    print("Spy Number")
else:
    print("Not Spy Number")