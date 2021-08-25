t = int(input())
while t:
    t -= 1
    i = 2
    line = int(input())
    print("1",end = "")
    for i in range(2,line+1):
        c = 0
        while( line % i == 0 ):
            c += 1
            line /= i
        if c :
            print(" * ",i,"^",c,end="",sep="")
    print("")

