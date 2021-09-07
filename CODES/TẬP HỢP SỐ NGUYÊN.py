line = input()
in1 = input()
in2 = input()

in1 = in1.split()
for i in range(len(in1)):
    in1[i] = int(in1[i])

in2 = in2.split()
for i in range(len(in2)):
    in2[i] = int(in2[i])
line1 = []
line2 = []

for i in set(in1):line1.append(i)
for i in set(in2):line2.append(i)

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
