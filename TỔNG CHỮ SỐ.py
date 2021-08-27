n = input()
flag = 0
# if(n[0] == '-'): # loai bo dau tru
#     n = n[1:len(n)]
#     flag = 1
# print(n)
def sum(n):
    temp = 0
    for i in n:
        if i == '-':
            temp += ord('-') - ord('0')
        else:
            temp += int(i)

    return str(temp)

if(len(n) == 1):
    print(1)
else:
    c=0
    while(len(n) != 1):
        c +=1
        # print(sum(n))
        n = sum(n)

    print(c)