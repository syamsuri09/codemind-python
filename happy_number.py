n = int(input())

sq = 0
while n : 
    f = n % 10 
    sq += f**2
    s = n // 10
    n = s 
    if n == 0 and sq//10!=0:
        n = sq
        sq = 0
if sq == 1 or sq==7 :
    print("True")
else:
    print("False")