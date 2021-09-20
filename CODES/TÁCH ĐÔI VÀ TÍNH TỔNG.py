def sum(n):
    num1 = n[0:len(n)//2]
    num2 = n[len(n)//2:]

    arr1 , arr2 = [],[]

    for i in num1:
        arr1.append(int(i))
    for i in num2:
        arr2.append(int(i))

    if(len(arr1) > len(arr2)):
        arr1 ,arr2 = arr2,arr1
    arr1.reverse()
    arr1.append(0)
    arr2.reverse()
    arr2.append(0)

    res = []
    remember = 0;
    temp = 0;

    for i in range(len(arr1)):
        temp = arr1[i] + arr2[i] + remember
        res.append( temp % 10)
        remember = temp // 10

    for i in range(len(arr1) , len(arr2)):
        temp = arr2[i] + remember
        res.append(temp % 10)
        remember = temp // 10

    res.reverse()

    while res[0] == 0:
        res.pop(0)

    strRes = ""
    for i in res:
        strRes += str(i)
    print(strRes)
    return res




n = input()
n = sum(n)
while len(n) > 1:
    n = sum(n)
