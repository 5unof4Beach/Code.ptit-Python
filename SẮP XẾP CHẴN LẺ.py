n = int(input())
# line = input()
count = 0
arr = []
while count<n:
    line = input()
    line = line.split()
    for i in line:
        count += 1
        arr.append(int(i))



hash = dict()
arr_le , arr_chan = [],[]

for i in range(0,n):
    if(arr[i] % 2 ==0):
        hash[i] = 0
        arr_chan.append(arr[i])
    else:
        hash[i] = 1
        arr_le.append(arr[i])

arr_chan.sort()
arr_le.sort(reverse=True)

temp_chan = 0
temp_le = 0
for j in hash:
    if(hash[j] == 0):
        arr[j] = arr_chan[temp_chan]
        temp_chan += 1
    else:
        arr[j] = arr_le[temp_le]
        temp_le += 1

print("")
for i in arr:
    print(i,"",end="")
