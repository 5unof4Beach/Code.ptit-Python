# import math
#
# from itertools import count, islice
# def isPrime(n):
#     if n<2: return False
#     for i in islice(count(2),int(math.sqrt(n)-1)):
#         if n%i == 0:
#             return False
#     return True

temp = int(input())
line = input()
line = line.split()
lst = []
for i in line:
    # if not isPrime(int(i)):
    lst.append(int(i))
n = max(lst)

#sang so nguyen to
pos = 1
num = [True for i in range(2 * n + 1)]
p = 2
while ( p * p <= 2 * n ): #tim trong khoang căn của 2 * n
    if num[p] == True:
        i = p * p
        while i <= n * 2:
            num[i] = False
            i += p
    p += 1
primes = []
for p in range(2, (2 * n) + 1):
    if num[p]:
        primes.append(p)
ans = 0
for i in range(len(line)):
    x = -1
    for j in range(len(primes)): # tim phan tu nto dau tien lon hon arr[i]
        if lst[i] == primes[j]:
            x = j
            break
        elif lst[i] < primes[j]:
            x = j # lay thu tu cua so nguyen to
            break
    minm = abs(primes[x] - lst[i])

    if (x > 1):
        minm = min(minm, abs(primes[x - 1] - lst[i]))
    ans = max(ans, minm)
print(ans)
# res =[]
# print(lst)
# for i in lst:
#     if i < 2:
#         res.append(2-i)
#     else:
#         for j in range(i,n*2 ):
#             if num[j]:
#                 print(i,":",j)
#                 res.append(min( abs(prime[num[j]] - i ) , abs(prime[num[j] - 1] - i) ))
#                 break
# res.sort(reverse=True)

# print(res[0])