n = input()

l = []
for i in n:
    l+=i
test = list(set(l))
if len(l) == len(test):
    print("Unique Number")
else:
    print("Not Unique Number")