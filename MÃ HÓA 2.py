P = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_.'

inp = input()
arr = inp.split()
k = int(arr[0])
line = arr[1]
res = []

while k :
    res.clear()
    for i in line:
        res.append(P[( P.find(i) + k) % 28])
    res.reverse()
    for i in res:
        print(i,end="")
    print("")

    inp = input()
    if(inp == '0'):
        break
    else:
        arr = inp.split()
        k = int(arr[0])
        line = arr[1]

