def pr(n):
    if(n>1):
        for i in range(2,int(n**0.5)+1):
            if(n%i==0):
                return 0
        return 1
    else:
        return 0
n=int(input())
if(pr(n)==1):
    a=str(n)
    for i in a:
        b=int(i)
        if(pr(b)!=1):
            print("Not Mega Prime")
            break
    else:
        print("Mega Prime")
else:
    print("Not Mega Prime")   