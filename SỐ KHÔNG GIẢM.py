T = int(input())
while T:
    num = input()
    flag = 1
    for element in range( 0 , len(num)-1 ):
        if(int( num[element] ) > int( num[element+1] )):
            print("NO")
            flag = 0
            break
    if flag:
        print('YES')
    T -= 1