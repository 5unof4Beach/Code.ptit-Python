
T = int(input())
while(T):

    # string = input()
    # hash = dict()
    # for element in string:
    #     if element in hash:
    #         hash[element] += 1
    #     else:
    #         hash[element] = 1
    #
    # for key in hash:
    #     print(hash[key],key,sep="",end="")
    # print("")
    T -= 1

    string = input()
    j = string[0]
    c = 0

    for i in string:
        if i==j :
            c += 1
        else:
            print(c,j,sep='',end='')
            j = i
            c = 1
    print(c,j,sep='')

