t = int(input())
while t:
    t-=1
    line = input()
    line = line.split()
    for i in range(0, len(line)):
        line[i] = float(line[i])
    n,x,m = line[0],line[1],line[2]
    c=1
    money = n + n*(x/100)
    while money < m:
        money += money * (x/100)
        c += 1

    print(c)

