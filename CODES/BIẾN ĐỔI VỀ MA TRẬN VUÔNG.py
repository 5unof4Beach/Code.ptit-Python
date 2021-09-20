line = input().split()
n = int(line[0])
m = int(line[1])
row = n
col = m
mat = []

if(n>m):
    for i in range(1,n+1):
        data = input()
        if(i % 2 == 1 and row != col):
            row -= 1
            continue
        else:
            mat.insert(i,data)

    for i in mat:
        print(i)
else:
    for i in range(0,n):
        data = input()
        mat.insert(i,data)
        mat[i] = mat[i].split()

    for i in range(0,n):
        col = m
        for j in range(0,m):
            if j%2 == 1 and row != col:
                col -= 1
                continue
            else:
                print(mat[i][j],end= " ")
        print()