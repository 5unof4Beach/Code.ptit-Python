line_1 = input()
c,n = 0,0

arr_1 = line_1.split()
q = []
tmp = len(arr_1)
for i in range(0, tmp):
    arr_1[i] = int(arr_1[i])
for i in set(arr_1): #do truong hop dac biet nhu 1 1 1 1  hay 2 2 2 2
    n = i            #nen phai check


while(n != 0 ): #neu nhap vao toan khong thi thoat vong lap
    c=0
    while( len(set(arr_1)) > 1 ):
        c += 1
        for i in range( 0,tmp ):
            if i == tmp - 1:
                q.append( abs(arr_1[i] - arr_1[0]) )
            else:
                q.append( abs(arr_1[i] - arr_1[i+1]) )

        for i in range( 0,tmp ):
            arr_1[i] = q.pop(0)
    print(c)

    # nhap case moi
    line_1 = input()
    arr_1 = line_1.split()
    tmp = len(arr_1)
    for i in range(0, tmp):
        arr_1[i] = int(arr_1[i])
    for i in set(arr_1):
        n = i

