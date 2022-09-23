a,b = map(int,input().split())

length = len(str(a))
index = str(a)[length-b:]
index_1 = str(a)[:b]
total = abs(int(index) - int(index_1))
print(total)