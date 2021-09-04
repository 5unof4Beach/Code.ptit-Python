t = int(input())

while t:
    t-=1

    n = input()
    res = 1
    for i in n:
        if(int(i)!=0):
            res *= int(i)
    print(res)