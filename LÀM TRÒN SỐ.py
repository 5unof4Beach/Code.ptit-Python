test = int(input())

while test:
    test -= 1
    s = input()
    s = list(s) #Vd so: 12345
    s.reverse()
    for i in range(0 , len(s)-1):
        if int(s[i]) >= 5:
            s[i+1] = int(s[i+1]) + 1
    print(s[-1],end="")
    for i in range(0,len(s)  - 1):
        print("0",sep="",end="")
    print("")