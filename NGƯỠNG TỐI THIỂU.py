line  = input()
k = int(input())
arr = []
n = len(line)
if(len(line) % 2 == 1):
    n -= 1
hash = dict()
arr = []
for i in range(0,n,2):
    if line[i:i+2] in hash:
        hash[line[i:i+2]] +=1
    else:
        hash[line[i:i+2]] = 1
        arr.append(line[i:i+2])
arr.sort()
flag = 1
for i in arr:
    if hash[i] >= k:
        flag = 0
        print(i,hash[i])
if flag:
    print("NOT FOUND")