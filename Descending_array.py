n = int(input())
arr = list(map(int,input().split()))

for i in range(len(arr)-1):
    t = arr[i] 
    s = arr[i+1]
    if t < s:
        print("no")
        break
else:
    print("yes")