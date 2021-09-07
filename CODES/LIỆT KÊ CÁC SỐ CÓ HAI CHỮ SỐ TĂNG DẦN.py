line  = input()
arr = []
n = len(line)
if(len(line) % 2 == 1):
    n -= 1

for i in range(0,n,2):
    arr.append(line[i:i+2])
arr = set(arr)

res = []
for i in arr:
    res.append(int(i))
res.sort()
for i in res:
    print(i,end= " ")