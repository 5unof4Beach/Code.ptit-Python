line = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
t = int(input())
while t:
    t -= 1
    temp = input()
    temp = temp.split()
    n , base = int(temp[0]),int(temp[1])
    res = []
    while(n != 0):
        res.append( n%base )
        n //= base
    # print(res)
    res.reverse()
    for i in res:
        print(line[ int(i) ], sep = '',end='')
    print('')

