n = int(input())
arr = list(map(str,input().split()))

c = ""
for i in range(0,len(arr),2):
    b = (arr[i]*int(arr[i+1]))
    c+=b
for j in c:
    print(j,end=" ")