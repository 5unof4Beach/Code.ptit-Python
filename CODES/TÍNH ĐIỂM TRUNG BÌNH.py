n = int(input())
n = input()
hash = dict()
arr = []
n = n.split();

for i in n: arr.append(float(i))

for i in arr:
    if i in hash:
        hash[i] += 1
    else:
        hash[i] = 1

hash_sorted = sorted(hash.keys())

sum = 0
for i in range(1,len(hash_sorted)-1):
    sum += hash_sorted[i] * hash[hash_sorted[i]]

sum /= len(arr) - hash[hash_sorted[0]] - hash[hash_sorted[len(hash_sorted)-1]]

print("{:.2f}".format(round(sum,2)))
