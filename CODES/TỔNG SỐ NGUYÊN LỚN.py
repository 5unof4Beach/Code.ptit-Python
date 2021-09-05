num1 = input()
num2 = input()
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
#loai bo tat ca so 0 o dau
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
else:
    for i in res:
        print(i,end="")




