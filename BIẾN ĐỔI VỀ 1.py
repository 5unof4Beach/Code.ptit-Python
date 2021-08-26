n = int(input())

while n:
    c = 1
    while(n != 1):
        if( n % 2 == 0):
            n=n/2
            c += 1
        else:
            n = n*3 + 1
            c += 1
    print(c)
    n = int(input())