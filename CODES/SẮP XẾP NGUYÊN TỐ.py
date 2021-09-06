import math


def isPrime(n):
    if n<2 : return 0
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i ==0:
            return 0
    return 1
arr = []
hash = dict()
n = input()
line = input().split()
for i in range(len(line)):
    line[i] = int(line[i])

for i in range( len(line) ):
    if isPrime(line[i]):
        arr.append(line[i])
        hash[i] = 1
    else:
        hash[i] = 0

arr.sort()
pos = 0
for i in range( len(line) ):
    if(hash[i]):
        print(arr[pos],end=" ")
        pos += 1
    else:
        print(line[i],end=" ")
