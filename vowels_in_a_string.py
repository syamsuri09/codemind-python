n = input()
vowel = input()

for i in n:
    if vowel in n:
        ind = n.index(vowel)
        print(True)
        print(ind)
        break
else:
    print("False")