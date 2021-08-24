def gcd(n_1,n_2):     #Boi chung nho nhat
    while(n_2 != 0):
        n_1,n_2 = n_2,n_1%n_2
    return n_1

def isCoprime(n_1,n_2):
    return ( gcd(n_1,n_2)==1 )

n = int(input())
line = input()
arr  = line.split()
for i in range(0,n):
    arr[i] = int(arr[i])

arr.sort()
for i in arr:
    for j in arr:
        if(isCoprime(i,j) and i<j): # i phai nho hon j thi moi in ra
            print(i,j)
