t = int(input())
while t:
    t -= 1
    line = input()
    sum = 0
    for i in line:
        sum += int(i)
    if(sum % 10 == 0):
        flag = 1
        for i in range( 0, len(line) - 1):
            if( abs(int( line[i+1]) - int( line[i] )) != 2):
                print("NO")
                flag = 0
                break

        if flag :
            print("YES")
    else:
        print("NO")

