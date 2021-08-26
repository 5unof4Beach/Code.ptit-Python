line = input()
line = line.split()
arr = []
for i in line:
    arr.append( int(i) % 42 )

arr = set(arr)
print("")
print(len(arr))