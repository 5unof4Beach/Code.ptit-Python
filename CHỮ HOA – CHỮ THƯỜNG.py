line = input()
c = 0
for i in line:
    if(i.islower()):c += 1

if(c >= len(line) - c): print(line.lower())
else: print(line.upper())