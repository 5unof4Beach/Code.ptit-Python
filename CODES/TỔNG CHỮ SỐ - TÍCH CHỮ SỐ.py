t = int(input())

while t:
    t-=1
    flag = 1
    n = input()
    sum = 0
    mul = 1
    for i in range(0,len(n)):
        if i % 2 == 0:
            sum += int( n[i] )
        else:
            if( n[i] != '0'):
                flag = 0
                mul *= int( n[i] )

    print(sum," ",end="")
    if flag == 1:
        print(0)
    else:
        print(mul)
