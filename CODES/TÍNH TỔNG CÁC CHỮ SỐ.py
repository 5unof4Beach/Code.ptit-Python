t = int(input())
while t:
    t -= 1
    line = input()
    list = []
    sum = 0

    for i in line:
        if i.isnumeric():
            sum += int(i)
        else:
            list.append(i)

    list.sort()
    for i in list :
        print(i,end="")
    print(sum)

