num1 = input()
num2 = input()
arr1 , arr2 = [],[]

for i in num1:
    arr1.append(int(i))
for i in num2:
    arr2.append(int(i))
pos = 0
# loại bỏ số 0 ở đầu cả 2 số lớn tránh trường hợp 0123 124
for i in range(0,len(arr1)):
    if arr1[i] != 0:
        pos = i
        break
arr1 = arr1[pos:]
pos = 0
for i in range(0,len(arr2)):
    if arr2[i] != 0:
        pos = i
        break
arr2 = arr2[pos:]

themDauTru = 0
if(len(arr1) < len(arr2)):
    arr1 ,arr2 = arr2,arr1
    themDauTru = 1
elif(len(arr1) == len(arr2)):
    for i in range(0,len(arr1)):
        if(arr1[i] > arr2[i]):
            break
        elif(arr1[i] < arr2[i]):
            arr1, arr2 = arr2, arr1
            themDauTru = 1
            break

arr1.reverse()
arr2.reverse()

remember = 0
res=[]
temp = 0
for i in range(0,len(arr2)):
    temp = arr1[i] - arr2[i] - remember
    res.append( (temp + 10) % 10)
    remember = abs( ((temp + 10) // 10) - 1)
for i in range(len(arr2),len(arr1)):
    temp = arr1[i] - remember
    res.append((temp + 10) % 10)
    remember = abs(((temp + 10) // 10) - 1)

res.reverse()
#loai bo so 0 o dau
pos = 0
allZero = 1
for i in range(0,len(res)):
    if res[i] != 0:
        allZero = 0
        pos = i
        break
res = res[pos:]

if allZero:
    print(0)
elif themDauTru:
    print("-",end="")
    for i in res:
        print(i,end="")
else:
    for i in res:
        print(i, end="")