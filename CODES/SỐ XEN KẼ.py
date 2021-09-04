t = int(input())

while t:
    t-=1
    flag = 1
    n = input()

    if(n[0] == n[1]): flag = 0
    if len(n) % 2 == 0: flag = 0
    else:
        for i in range(2,len(n),2):
            if n[i] != n[0]:
                flag = 0
                break

    if flag:
        print("YES")
    else:
        print("NO")