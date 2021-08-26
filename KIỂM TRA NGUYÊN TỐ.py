import math

line = input();
line = line.split()
row,col = int(line[0]),int(line[1])
line = input()
line = line.split()

def isPrime(n):
    if n<2:return 0
    for i in range(2, int(math.sqrt(n))):
        if n % i == 0:
            return 0
    return 1

for i in range(0,len(line)):
    line[i] = isPrime(int(line[i]))
print(line)

# for i in range(0,row):
#     for j in range(0,col):
