num1 = input()
num2 = input()
arr1 , arr2 = [],[]

for i in num1:
    arr1.append(int(i))
for i in num2:
    arr2.append(int(i))
# print(arr1)
if(len(arr1) > len(arr2)):
    arr1 ,arr2 = arr2,arr1
arr1.reverse()
arr1.append(0)
arr2.reverse()
arr2.append(0)
# print(arr1)
# print(arr2)
res = []
remember = False;
temp = 0;
# if(len (arr1) < len(arr2)):
for i in range(len(arr1)):
    temp = arr1[i] + arr2[i];
    if remember:
        res.append((temp + 1) % 10 )
        if temp + 1 > 9:
            remember = True
        else:
            remember = False
    else:
        res.append(temp % 10)
        if temp > 9:
            remember = True
        else:
            remember = False

for i in range(len(arr1) , len(arr2)):
    if remember:
        if(arr2[i]+1 > 9):
            res.append((arr2[i]+1) % 10)
            remember = True
        else:
            res.append(arr2[i] + 1)
            remember = False
    else:
        res.append(arr2[i] % 10)
# print(res)
# kien tra xem kqua co bang 0 khong
def allZero(list):
    first = list[0]
    if first != 0:
        return False

    for i in list:
        if i != first:
            return False
    return True


res.reverse()
if(res[0] == 0):
    res.pop(0)

if allZero(res):
    print(0)
else:
    for i in res:
        print(i,end="")



