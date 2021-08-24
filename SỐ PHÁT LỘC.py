T = int(input())
while(T):
    line = input()
    # print(line[-1],line[-2])
    s = line[len(line) - 2:len(line)]
    # if(line[-2] == '8' and line[-1] == '6'):
    if(s == '86'):
        print("YES")
    else:
        print("NO")
    T -= 1