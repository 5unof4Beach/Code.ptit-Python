import math

line = input().split()
r = int(line[0])
c = int(line[1])
mat = []
primes = []
def isTN(n):
    if n<11: return False
    temp = str(n)
    temp2 = temp[::-1]
    if(temp == temp2):return True
    return False

not_found = 1

for i in range(r):
    temp = input()
    mat.insert(i,temp)
    mat[i] = mat[i].split()
    for j in mat[i]:
        if isTN(int(j)):
            not_found = 0
            primes.append(int(j))

if not_found:
    print("NOT FOUND")
else:
    max = max(primes)
    print(max)
    for i in range(r):
        for j in range(c):
            if int(mat[i][j]) == max:
                print("Vi tri ","[",i,"]","[",j,"]",sep="")



