t = int(input())
while t :
    t-=1
    f_0 , f_1 , sum = 1,1,0

    line = input()
    line = line.split()
    start , end = int(line[0]) , int(line[1])

    list = [0,1,1]

    for i in range(0,end):
        sum = f_0 + f_1
        list.append(sum)
        f_0 = f_1
        f_1 = sum

    for i in range(start , end+1):
        print(list[i]," ",end="")
    print("")

