n = int(input())
mat = []
#nhap ma tran
for i in range(0,n):
    temp = input()
    mat.insert(i,temp)
    mat[i] = mat[i].split()

k = int(input())
sum_up = 0
sum_beneath = 0

for i in range(0 , n-1):
    for j in range(i+1,n):
        sum_up += int( mat[i][j] )
        sum_beneath += int(mat[n-i-1][n-j-1])
res = abs(sum_up - sum_beneath)
if( res > k ):
    print("NO")
    print(res)
else:
    print("YES")
    print(res)