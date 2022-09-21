x = input()

sq = int(x) ** 2

reverse_x = ""
reverse_y = ""
for i in x:
    reverse_x = i + reverse_x
squ = int(reverse_x) ** 2
for q in str(squ):
    reverse_y = q + reverse_y
if str(sq) == reverse_y:
    print("True")
else:
    print("False")