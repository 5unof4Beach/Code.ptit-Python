def dfs(p,q):
    while q:
        p,q = q,p%q
    return p

def isCoprime(p,q):
    return ( dfs(p,q) == 1)

def isPrime(n):
    if n>1:
        for i in range( 2,int(n/2) + 1):
            if n%i == 0:
                return 0
        return 1
t = int(input())
while t:

    n = int(input())
    c = 0
    for i in range(1,n):
        if(isCoprime(i,n)):c += 1
    if isPrime(c):
        print("YES")
    else:
        print("NO")


    t-=1


