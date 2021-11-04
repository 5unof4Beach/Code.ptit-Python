s = input().split()
r = int(s[0])
c = int(s[1])
a = [[int(j) for j in input().split()] for i in range(r)]

maxN = -100000000

for i in range(r):
    temp = max(a[i])
    if temp > maxN:
        maxN = temp
done = False
for i in range(r):
    for j in range(c):
        if a[i][j] == maxN:
            print(i,j)
            done = True
            break
    if done:
        break



