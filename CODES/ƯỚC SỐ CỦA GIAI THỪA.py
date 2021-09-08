def biggestPow(n,p):
    res = 0
    while(n>0):
        n /= p
        res += int(n)
    return res

t = int(input())
while t:
    t-=1
    line = input().split()
    print( biggestPow (int(line[0]) , int(line[1])) )