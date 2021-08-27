import math

mat = []
n = int(input())
sum = 0
# nhập và tính cặp các hàng
for i in range(0,n):
    count=0
    temp = input()
    mat.insert(i,temp)
    for j in mat[i]:
        if j == 'C':
            count += 1
    sum += math.comb(count,2)

# tính cặp các cột
for i in range(0,n):
    count = 0
    for j in range(0,n):
        if mat[j][i] == 'C':
            count +=1
    sum += math.comb(count,2)

print(sum)

# print(mat)
#
# i = math.comb(4,2)
# print(i)