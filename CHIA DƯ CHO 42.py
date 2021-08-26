line = input()
line = line.split()
arr = []
for i in line:
    arr.append( int(i) % 42 )
c=0
hash = dict()
for i in arr:
    if i in hash:
        hash[i] +=1
    else:
        hash[i] = 1

for key in hash:
    c += 1
print("")
print(c)
# arr = set(arr)
# print("")
# print(len(arr))