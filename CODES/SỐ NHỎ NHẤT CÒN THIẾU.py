n = int(input())
line = input().split()
for i in range(0,n):
    line[i] = int(line[i])
flag = 1
for i in range(0, n-1):
    if(line[i+1] - line[i] > 1 ):
        print(line[i] + 1)
        flag = 0
        break
    elif(line[i] - line[i+1] < -1):
        print(line[i+1]+1)
        flag = 0
        break

if flag :
    print(line[n-1] + 1)

# print(line)