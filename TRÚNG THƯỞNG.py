t = int(input())
while t:
    t-=1
    n = int(input())
    arr = []
    hash = dict()

    while n:
        n -= 1
        arr.append(int(input()))
    for i in arr:
        if i in hash:
            hash[i] += 1
        else:
            hash[i] = 1
    arr.clear()

    # tim so lan xuat hien nhieu nhat
    max_val = 0
    for key in hash:
        if hash[key] > max_val:
            max_val = hash[key]

    #tim stt nho nhat trong so nhung stt xuat hien nhieu nhat
    min_val = 1001
    for key in hash:
        if hash[key] == max_val:
            if key < min_val:
                min_val = key
    print(min_val)


