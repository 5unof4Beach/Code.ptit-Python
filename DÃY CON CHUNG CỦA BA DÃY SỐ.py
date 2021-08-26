t = int(input())
while(t):
    t-=1

    line = input()
    line = line.split()
    n1,n2,n3 = int(line[0]),int(line[1]),int(line[2])
    arr1,arr2,arr3 = input(),input(),input()
    arr1 = arr1.split()
    arr2 = arr2.split()
    arr3 = arr3.split()
    for i in range(0,len(arr1)): arr1[i] = int(arr1[i])
    for i in range(0, len(arr2)): arr2[i] = int(arr2[i])
    for i in range(0, len(arr3)): arr3[i] = int(arr3[i])

    i,j,k = 0,0,0
    flag = 1
    while(i<n1 and j<n2 and k<n3):
        if (arr1[i]==arr2[j] and arr2[j]==arr3[k]):
            flag = 0
            print(arr1[i],"",end="")
            i += 1
            j += 1
            k += 1
        elif arr1[i] < arr2[j]:
            i += 1
        elif arr2[j] < arr3[k]:
            j += 1
        else:
            k += 1
    if flag:
        print("NO",end="")
    print("")

