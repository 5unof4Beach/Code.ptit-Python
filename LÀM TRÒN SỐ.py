def my_print(num, n):
    print(num,end="")
    for i in range(0,n):
        print("0",sep="",end="")
    print("")

t = int(input())
while t:
    s = input()
    if (s == '5'):
        print(5)
        continue


    if s[-1] == '5':
        if s[0] == '9':
            my_print( 1,len(s) )
        else:
            my_print( int(s[0])+1, len(s)-1 )

    else:
        if( int( s[1] ) >= 5 ):
            if s[0] == '9':
                my_print(1, len(s))
            else:
                my_print( int(s[0]) + 1, len(s) - 1 )
        else:
            my_print( int(s[0]), len(s) - 1 )

    t-=1