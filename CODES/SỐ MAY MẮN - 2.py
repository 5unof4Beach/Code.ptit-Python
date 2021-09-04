test = int(input())
while test > 0:
    test -= 1
    n = input()
    check = 1
    for i in n:
        if i != '4' and i != '7':
            check = 0
            break
    if check == 1:
        print("YES")
    else:
        print("NO") #comment