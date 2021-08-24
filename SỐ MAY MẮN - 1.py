num = input()
c=0
for element in num:
    if( element == '4' or element == '7'): c += 1
if (c == 4 or c == 7):
    print("YES")
else:
    print("NO")