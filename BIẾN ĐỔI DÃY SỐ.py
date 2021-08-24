# line_1,line_2= input(), input()
line_1 = input()
c = 0

arr_1 = line_1.split()
# arr_2 = line_2.split()
q = []
tmp = len(arr_1)
for i in range(0, tmp):
    arr_1[i] = int(arr_1[i])
    # arr_2[i] = int(arr_2[i])

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


# c=0
# while( len(set(arr_2)) > 1 ):
#     c += 1
#     for i in range( 0,tmp ):
#         if i == tmp - 1:
#             q.append( abs(arr_2[i] - arr_2[0]) )
#
#         else:
#             q.append( abs(arr_2[i] - arr_2[i+1]) )
#
#     for i in range( 0,tmp ):
#         arr_2[i] = q.pop(0)
#
#
# print(c)

