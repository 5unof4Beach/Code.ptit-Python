lst = [15,4,5,6,7,200,50]
print("Bai 3 :")
for i in lst:
    if i <= 150:
        if i % 5 == 0:
            print(i)
    else:
        break

print("Bai 4:")
n = int(input())
if( n == 1):
    print(n,"st",sep="")
elif( n == 2):
    print(n,"nd",sep="")
if( n == 3):
    print(n,"rd",sep="")
else:
    print(n,"th",sep="")