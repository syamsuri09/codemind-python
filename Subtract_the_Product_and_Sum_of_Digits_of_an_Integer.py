x = input()

add = 0
mul = 1
for i in x:
    add += int(i)
    mul *= int(i)
total = mul - add

print(total)