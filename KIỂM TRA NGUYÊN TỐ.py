import math


def isPrime(n):
    n = int(n)
    if n < 2 : return 0
    for i in range( 2 , int(n/2)+1):
        if(n % i == 0): return 0
    return 1

line = input();
line = line.split()
row,col = int(line[0]),int(line[1])
mat = []

for i in range(0,row):
    temp = input()
    mat.insert(i,temp) #insert( pos , value )
    mat[i] = mat[i].split()
    for j in mat[i]:
        j = isPrime(j)
        print(j,"",end="")
    print("")
