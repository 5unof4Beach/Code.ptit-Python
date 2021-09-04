count = 0
arr = []
while count<10:
    line = input()
    line = line.split()
    for i in line:
        count += 1
        arr.append(int(i) % 42)

# print(line)

c=0
hash = dict()
for i in arr:
    if i in hash:
        hash[i] +=1
    else:
        hash[i] = 1

for key in hash:
    c += 1
# print("")
print(c)
