
t = int(input())
while(t):

    line = input()
    i=0
    for i in range(0,len(line)):
        if(line[i].isnumeric()):
            for j in range(0 , int(line[i])):
                print(line[i-1],end='')
    print("")
    t-=1
