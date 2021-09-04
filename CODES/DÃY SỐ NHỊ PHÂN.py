n = int(input())
line = input()
arr = []
line = line.split()
c = 0
for i in range( 0 , n-1):
    if(line[i] != line[i+1]):
        c += 1

print(c)


