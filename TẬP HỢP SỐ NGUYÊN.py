line = input()
line = line.split()
n1 , n2 = int(line[0]),int(line[1])
line1 = input()
line2 = input()
line1 = line1.split()
line1 = set(line1)
line2 = line2.split()
line2 = set(line2)
arr = []
for i in line1: arr.append(i)
for i in line2: arr.append(i)

hash = dict()

for i in arr:
    if i in hash:
        hash[i] += 1
    else:
        hash[i] = 1
arr.clear()

for key in hash:
    if hash[key] == 2:
        print(key,"",end="")
print("")
for i in line1:
    if hash[i] == 1:
        print(i,"",end="")
print("")
for i in line2:
    if hash[i] == 1:
        print(i,"",end="")
