n = int(input())
line = input()
arr = line.split()
hash = dict()

def isPrime(num):
    if num > 1:
        for i in range( 2 , int(num / 2) + 1):
            if  (num % i == 0):
                return 0
    return 1

for i in range(0,len(arr)):
    arr[i] = int(arr[i])

for element in arr:
    if element in hash:
        hash[element] += 1
    else:
        hash[element] = 1

for key in hash:
    if isPrime(key):
        print(key,hash[key])