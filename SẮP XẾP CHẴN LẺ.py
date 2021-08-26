n = int(input())
line = input()
line = line.split()
for i in range( 0, n):
    line[i] = int(line[i])

hash = dict()
arr_le , arr_chan = [],[]

for i in range(0,n):
    if(line[i] % 2 ==0):
        hash[i] = 0
        arr_chan.append(line[i])
    else:
        hash[i] = 1
        arr_le.append(line[i])

arr_chan.sort()
arr_le.sort(reverse=True)

temp_chan = 0
temp_le = 0
for j in hash:
    if(hash[j] == 0):
        line[j] = arr_chan[temp_chan]
        temp_chan += 1
    else:
        line[j] = arr_le[temp_le]
        temp_le += 1

for i in line:
    print(i," ",end="")