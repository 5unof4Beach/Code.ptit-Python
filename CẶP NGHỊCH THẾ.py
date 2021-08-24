n = int(input())
line = input()
count = 0

list = line.split(" ")
for i in range(0,n):
    list[i] = int(list[i])
# print(list)

for i in range(0,n-1):
    j = i+1
    for j in range(i+1,n):
        if( list[i]>list[j] ): count += 1

print(count)
