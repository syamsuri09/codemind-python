s,t,b = list(map(int,input().split()))

capacity = 2 * s * t * b * 512
total = capacity // 1024

print("{}KB".format(total))