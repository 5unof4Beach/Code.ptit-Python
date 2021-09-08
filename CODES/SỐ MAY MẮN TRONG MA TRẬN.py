import math

line = input().split()
r = int(line[0])
c = int(line[1])
mat = []
primes = []
def isPrime(n):
    if n<2: return 0
    for i in range(2,int( math.sqrt(n) + 1 )):
        if n%i == 0:return 0
    return 1

not_found = 1

for i in range(r):
    temp = input()
    mat.insert(i,temp)
    mat[i] = mat[i].split()
    for j in mat[i]:
        primes.append(int(j))
max = max(primes) - min(primes)


if primes.count(max) == 0:
    print("NOT FOUND")
else:
    print(max)
    for i in range(r):
        for j in range(c):
            if int(mat[i][j]) == max:
                print("Vi tri ","[",i,"]","[",j,"]",sep="")



