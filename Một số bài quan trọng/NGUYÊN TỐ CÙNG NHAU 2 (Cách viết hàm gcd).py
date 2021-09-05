def gcd(a,b):
    if(b == 0):
        return a
    else:
        return gcd(b,a%b)

def isCoprime(a,b):
    if gcd(a,b) == 1:
        return 1
    return 0

n1 = input()
n1 = n1.split()
n = int(n1[0])
num = int(n1[1])

c= 0
for i in range(10**(num-1),10**num-1):
    if isCoprime(n,i):
        c += 1
        print(i,"",end="")
    if c == 10:
        print("")
        c = 0