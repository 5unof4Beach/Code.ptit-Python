P = 'abcdefghijklmnopqrstuvwxyz'
t = int(input())
while t:
    t-=1

    line = input()
    temp = int(len(line)/2)
    flag = 1

    line_reverse = line[ : :-1]  # [start : stop : step ]

    for i in range( 0 , temp + 1): # chi kiem tra den qua nua chuoi thoi
        if( abs( P.find(line_reverse[i]) - P.find(line_reverse[i+1]) ) != abs( P.find(line[i]) - P.find(line[i+1]) ) ):
            print("NO")
            flag = 0
            break

    if(flag):
        print("YES")

