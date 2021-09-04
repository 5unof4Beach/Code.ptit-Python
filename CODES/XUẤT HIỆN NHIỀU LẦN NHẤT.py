T = int(input())
while( T ):
    max,num = 0,0
    n = int(input())
    line = input()

    arr = line.split(" ")
    for i in range(0,n):
        arr[i] = int(arr[i])

    hash = dict()
    for element in arr:
        if element in hash:
            hash[element] += 1  #pair  key     : value
        else:                   #      element : occurence
            hash[element] = 1

    for key in hash:
        if(hash[key]>max):
            max = hash[key]
            num = key

    if(max > n/2):
        print(num)
    else:
        print("NO")

    T -= 1

