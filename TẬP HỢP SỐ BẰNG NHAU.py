n = input()

line1,line2 = input(),input()

line1 = line1.split()
# for i in range( 0 ,len(line1)): line1[i] = int(line1)
line2 = line2.split()
# for i in range( 0 ,len(line2)): line2[i] = int(line2)
line1 = set(line1)
line2 = set(line2)
arr1,arr2 = [],[]
for i in line1:
    arr1.append(i)
arr1.sort()
for i in line2:
    arr2.append(i)
arr2.sort()

flag = 1
if len(arr1) == len(arr2):
    for i in range(0,len(arr1)):
        if(arr1[i] != arr2[i]):
            print("NO")
            flag = 0
            break
    if flag: print("YES")
else: print("NO")


