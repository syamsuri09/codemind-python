n = input()

c = 0
d = 0
for i in n:
    if i == " ":
        c +=1
    d+=1

print(abs(c-d))