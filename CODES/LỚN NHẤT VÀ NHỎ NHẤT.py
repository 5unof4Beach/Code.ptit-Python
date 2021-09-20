def isGreater(n1,n2):
    if len(n1) > len(n2):
        return True
    elif len(n1) < len(n2):
        return False
    return n1 > n2

while True:
    n = int(input())
    if n == 0:
        break
    max = '0'
    min = ''

    for i in range(n):
        temp = input()
        while temp[0] == '0':
            temp = temp.lstrip('0')
        if isGreater(temp,max):
            max = temp
        if len(min) == 0 or isGreater(min,temp):
            min = temp
    if(max == min): print("BANG NHAU")
    else: print(min," ",max)

