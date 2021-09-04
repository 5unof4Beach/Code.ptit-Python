line  = input()
sum = 0
c = 0
for element in line:
    if(element.isnumeric() and c<2):
        sum += int(element)
        c += 1
    elif(element.isnumeric() and c>=2):
            if(sum == int(element)):
                print("YES")
            else:print("NO")

# print(sum)