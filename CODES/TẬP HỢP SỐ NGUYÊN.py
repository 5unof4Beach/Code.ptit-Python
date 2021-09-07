line = input()
line1 = input()
line2 = input()

line1 = line1.split()
for i in range(len(line1)):
    line1[i] = int(line1[i])
    
line2 = line2.split()
for i in range(len(line2)):
    line2[i] = int(line2[i])
line1.sort()
line2.sort()

arr = []
for i in line1:
    if i in line2:
        print(i,end=" ")
        arr.append(i)
print()
for i in line1:
    if i not in arr:
        print(i,end=" ")
print()
for i in line2:
    if i not in arr:
        print(i,end=" ")
