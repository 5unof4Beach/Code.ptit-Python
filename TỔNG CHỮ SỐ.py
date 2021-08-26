n = input()
if(n[0] == '-'):
    n = n[1:len(n)]

# print(n)
def sum(n):
    temp = 0
    for i in n:
        temp += int(i)
    return str(temp)
c=0
while(len(n) != 1):
    c +=1
    n = sum(n)

print(c)