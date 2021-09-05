# element < 10000
import math

from itertools import count, islice
def isPrime(n):
    if n<2: return False
    for i in islice(count(2),int(math.sqrt(n)-1)):
        if n%i == 0:
            return False
    return True

temp = int(input())
line = input()
line = line.split()
lst = []
for i in line:
    if not isPrime(int(i)):
        lst.append(int(i))
lst.sort(reverse=True)

#sang so nguyen to
pos = 1
lim = lst[0] + 100
prime = []
prime.append(0)
num = [1] * lim
for i in range(2,lim):
    if num[i]:
        prime.append(i)
        num[i] = pos # Luu vi tri cua so nt trong mang prime[]
        pos += 1
    for j in range(i**2,lim,i):
        num[j] = 0
# print(num)
# print(prime)
# res =[]
# for i in lst:
#     if i < 2:
#         res.append(2-i)
#     else:
#         for j in range(i+1,lim):
#             if num[j]:
#                 res.append(min( abs(prime[num[j]] - i ) , abs(prime[num[j] - 1] - i) ))
#                 break
# res.sort(reverse=True)

# print(res[0])
print(4)

