line  = input()
arr = []
n = len(line)
if(len(line) % 2 == 1):
    n -= 1
hash = dict()
for i in range(0,n,2):
    if line[i:i+2] in hash:
        continue
    else:
        hash[line[i:i+2]] = 1
        arr.append(line[i:i+2])
for i in arr:
    print(i,end=" ")
