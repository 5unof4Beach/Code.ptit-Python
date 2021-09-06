t = int(input())
while t:
    t -= 1
    num = input()
    sum = 0
    for i in num:
        sum += int(i)
    if(sum<10):
        print("NO")
    else:
        sum = str(sum)
        sum_revt = sum[::-1]
        if(sum == sum_revt):
            print("YES")
        else:
            print("NO")