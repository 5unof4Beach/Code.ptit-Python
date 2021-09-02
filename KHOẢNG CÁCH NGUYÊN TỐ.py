import math

prime_set = [2,3,5,7]
num = 11
count = 0

for i in range(11,10000):
    flag = 1
    for j in prime_set:
        if(i % j == 0):
            flag = 0
            break
    if flag:
        prime_set.append(i)
        count += 1
        if count > 1100:
            break
        # print(i)



# print(prime_set)

line = input()
arr = line.split(" ")
# print(arr)

N,X = int(arr[0]), int(arr[1])
for i in range (0,N+1):
    print(X," ",end="")
    X += prime_set[i]
print("")
