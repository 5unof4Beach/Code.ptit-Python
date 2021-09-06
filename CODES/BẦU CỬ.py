line = input()
line = input().split()
hash = dict()
line.sort()

for i in line:
    if i in hash:
        hash[i] += 1
    else:
        hash[i] = 1

hash_sorted = sorted(hash.items(), key = lambda x:x[1], reverse=True)
# print(hash_sorted)
allEqual = 1
max = max(hash.values())
# print(max)
for key in hash:
    if hash[key] != max:
        allEqual = 0
        break

# print(hash_sorted)
if allEqual:
    print("NONE")
else:
    for i in hash_sorted:
        if i[1]<max:
            print(i[0])
            break

