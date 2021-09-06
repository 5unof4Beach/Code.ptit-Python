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

allEqual = 1

#kiem tra xem so phieu bau co bang nhau hay khong
max = max(hash.values())
for key in hash:
    if hash[key] != max:
        allEqual = 0
        break

if allEqual:
    print("NONE")
else:
    for i in hash_sorted:
        if i[1]<max:
            print(i[0])
            break

