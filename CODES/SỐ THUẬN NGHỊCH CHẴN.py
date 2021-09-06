t = int(input())
while t:
    t -= 1

    n = int(input())
    for i in range(22,n,22):
        count = 0 # so cac chu so
        flag = 1
        num = 0 # so nghich dao
        m = i
        while m > 0:
            temp = m % 10
            count += 1
            if temp % 2 != 0:
                flag = 0
                break
            num = num*10 + temp
            m //= 10
        if flag and count % 2 == 0 and num == i:
            print(i,end=" ")
    print("")


