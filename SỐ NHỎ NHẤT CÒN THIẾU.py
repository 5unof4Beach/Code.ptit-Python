n = int(input())
line = input()
line = line.split()
arr = []
arr.append(0)
# temp = len(line)
for i in range(0 , n):
    arr.append(int(line[i]))
flag = 1

for i in range(0, n ):
    if(arr[i+1] - arr[i] > 1 ):
        print(arr[i] + 1)
        flag = 0
        break

if flag :
    print(arr[n] + 1)

# print(line)