t = int(input())
while(t):
    t-=1

    line = input().split()
    n1,n2,n3 = int(line[0]),int(line[1]),int(line[2])
    arr1,arr2,arr3 = input(),input(),input()
    arr1 = arr1.split()
    arr2 = arr2.split()
    arr3 = arr3.split()

    arr1_rep = arr1
    for i in range(0,len(arr1_rep)): arr1_rep[i] = int(arr1_rep[i])
    arr2_rep = arr2
    for i in range(0, len(arr2_rep)): arr2_rep[i] = int(arr2_rep[i])
    arr3_rep = arr3
    for i in range(0, len(arr3_rep)): arr3_rep[i] = int(arr3_rep[i])


    arr1,arr2,arr3 = set(arr1),set(arr2),set(arr3)

    hash = dict()

    for i in arr1:
        if i in hash:
            hash[i] += 1
        else:
            hash[i] = 1

    for i in arr2:
        if i in hash:
            hash[i] += 1
        else:
            hash[i] = 1

    for i in arr3:
        if i in hash:
            hash[i] += 1
        else:
            hash[i] = 1
    flag = 1
    res = []
    for key in hash:
        if hash[key] == 3:
            res.append(int(key))
            flag = 0
    if flag == 0:
        res.sort()
        for i in res:
            c1,c2,c3= 0,0,0
            flag_2 = 1
            for j in arr1_rep:
                if i == j: c1 += 1
            for j in arr2_rep:
                if i == j: c2 += 1
            if c1 == c2:
                for j in arr3_rep:
                    if i == j: c3 += 1
                if c1 == c3:
                    flag_2 = 0
                    for k in range(0,c3):
                        print(i,"",end="")
            if flag_2:
                print(i,"",end="")
    else: print("NO",end="")
    print("")



