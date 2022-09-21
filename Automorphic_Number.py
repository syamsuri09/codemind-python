n = int(input())

a = n **2

num = str(n)

n_number = len(num)

change = str(a)

length = len(change)

last_digit = change[length-n_number:]
if last_digit == num :
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")