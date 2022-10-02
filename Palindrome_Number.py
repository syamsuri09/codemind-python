n = int(input())

for i in range(n):
    x = input()
    pali = x[::-1]
    if pali == x:
        print("True")
    else:
        print("False")