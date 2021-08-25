line = input()

arr = line.split()
for i in range(0,len(arr)):
    arr[i] = int(arr[i])

c=1
temp = arr[1]
res = []

while(temp <= arr[2]):

    c += 1
    temp = arr[1] * c
    if( arr[1]*c > arr[2] ): break
    if ( arr[1]*c - arr[0] > 0 ):
        res.append(arr[1]*c - arr[0] )

if(len(res)==0):
    print(-1)
else:
    for element in res:
        print(element," ",end="")