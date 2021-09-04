t = int(input())
c = 0
while t:
    t -= 1
    c += 1
    line1,line2 = [],[]
    temp = input()
    line1 = [i for i in temp]

    temp = input()
    line2 = [i for i in temp]

    line1.sort()
    line2.sort()
    # print(line1)
    # print(line2)
    flag = 1
    if(len(line2) == len(line1)):
        for i in range(0,len(line2)):
            if(line2[i] != line1[i]):
                print("Test",c,end='')
                print(": NO")
                flag = 0
                break
        if flag:
            print("Test", c, end='')
            print(": YES")
    else:
        print("Test", c, end='')
        print(": NO")
