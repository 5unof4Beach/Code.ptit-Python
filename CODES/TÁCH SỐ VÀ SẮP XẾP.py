t = int(input())
res = []
while t:
    t-=1
    line = input()
    for i in line:
        if i.isalpha():
            line = line.replace(i," ") # cai nao la chu thi thay = dau cach
    line = line.split()
    #loai bo so khong o dau
    for j in line:
        res.append(int(j))
        
res.sort()
for i in res:
    print(i)

