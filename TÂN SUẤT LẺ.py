t = int(input())
while t:
    t -= 1
    n = int(input())
    line = input()
    line = line.split()
    hash = dict()

    for i in line:
        if i in hash:
            hash[i] += 1
        else:
            hash[i] = 1

    for key in hash:
        if hash[key] % 2 == 1:
            print(key)

