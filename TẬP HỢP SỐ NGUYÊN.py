line = input()
line = line.split()
n1 , n2 = int(line[0]),int(line[1])
line1 = input()
line2 = input()
line1 = line1.split()
line2 = line2.split()

for i in range(0, len(line1)): line1[i] = int(line1[i])
for i in range(0, len(line2)): line2[i] = int(line2[i])
line1.sort()
line2.sort()

arr , arr_rep= [],[]
i,j = 0,0
while(i<n1 and j<n2):
    if line1[i] == line2[j]:
        print(line1[i],"",end="")
        arr.append(line1[i])
        arr_rep.append(line1[i])
        i += 1
        j += 1
    elif line1[i] < line2[j]:
        i += 1
    else:
        j += 1
print("")

arr.append(0)
arr_rep.append(0)
flag = 0
temp = 0
for i in line1:
    flag = 1
    # print(i,"",end="")
    for j in arr:
        if i == j:
            flag = 0
            arr.remove(j)
            # print(arr)
    if flag:
        print(i,"",end="")
print("")

# print(arr_rep)
for i in line2:
    flag = 1
    for j in arr_rep:
        if i == j:
            flag = 0
            arr_rep.remove(j)
    if flag:
        print(i,"",end="")
print("")