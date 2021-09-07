line  = input()
arr = []
n = len(line)
if(len(line) % 2 == 1):
    n -= 1
hash = dict()
for i in range(0,n,2):
    if line[i:i+2] in hash:
        hash[line[i:i+2]] +=1
    else:
        hash[line[i:i+2]] = 1

for key in hash:
    print(key,hash[key])
