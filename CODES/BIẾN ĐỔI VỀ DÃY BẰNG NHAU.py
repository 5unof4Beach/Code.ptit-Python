n = int(input())
inp = input().split()
line = []
avg = 0
for i in inp:
    line.append( int(i) )
hash = dict()
for i in line:
    sum = 0
    for j in line:
        sum += abs(i-j)
    hash[i] = sum
hash_sorted = sorted(hash.items(),key = lambda x:x[1])
print(hash_sorted[0][1],hash_sorted[0][0])
