T = int(input())
while(T):

    n = int(input())
    line_1, line_2 = input(), input()
    arr_1, arr_2 = line_1.split(), line_2.split()
    flag = 1
    arr_1.sort()
    arr_2.sort()
    for i in range(0,n):
        if(arr_1[i] > arr_2[i]):
            print("NO")
            flag = 0
            break
    if(flag):
        print("YES")

    T -= 1

    # for i in range (0,n):
#     arr_1[i] = int(arr_1[i])
    #     arr_2[i] = int(arr_2[i])











