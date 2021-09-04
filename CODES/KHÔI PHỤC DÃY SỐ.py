n = int(input())
arr = []
if(n == 2): # trường hợp ma trận 2x2
    while n:
        n -= 1
        line = input()
        arr.append(line)
    for i in range(len(arr)):
        arr[i] = arr[i].split()
    print( int(arr[0][1])//2 , int(arr[0][1])//2 )
else:
    n = 2 # chỉ cần lấy 2 dòng của ma trận là đủ để tìm ra dãy số gốc
    while n:
        n -= 1
        line = input()
        arr.append(line)
    for i in range(len(arr)):
        arr[i] = arr[i].split()

    res = []
    n1 =( int(arr[0][1]) + int(arr[1][2]) - int(arr[0][2]) ) // 2
    res.insert(1,n1) #tim n[1] va them vao res
    res.insert(0,int(arr[0][1]) - n1) #tim n[0] va them vao res
    for i in range(len(arr[0]) - 2):
        res.append( int(arr[0][i+2]) - res[0] )

    for i in res:
        print(i,"",end="")
