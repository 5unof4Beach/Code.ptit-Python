
t = int(input())
while t:

    line = input()
    if(line[0] == line[-2] and line[1] == line[-1]):
        print("YES")
    else:
        print("NO")
    t -= 1