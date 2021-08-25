T = int(input())
while(T):

    n = int(input())
    line_1, line_2 = input(), input()
    arr_1, arr_2 = line_1.split(), line_2.split()
    flag = 1
    pos = []
    c=0
    for i in range(0,n):
        if(arr_1[i] > arr_2[i]):
            temp = i
            break
    for i in range(0, n):
        if((arr_1[i] <= arr_2[i])):
            #swap
            num = arr_1[i]
            arr_1[i] = arr_1[temp]
            arr_1[temp] = num
            break

    for i in range(0, n):
        if ((arr_1[i] > arr_2[i])):
            temp = i

    for i in range(0, n):
        if(i == temp ):
            continue
        else:
            if(arr_2[i] >= arr_1[temp] and arr_2[temp] >= arr_1[i]):
                num = arr_2[i]
                arr_2[i] = arr_2[temp]
                arr_2[temp] = num
    print(arr_1)
    print(arr_2)
    
    for i in range(0,n):
        if(arr_1[i] > arr_2[i]):
            print("NO")
            flag = 0
            break
    if flag:
        print("YES")
    T -= 1













