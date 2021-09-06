line  = input()
# s = input()

line = line.replace("688","")
line = line.replace("68","")
line = line.replace("6","")
if len(line) == 0:
    print("YES")
else:
    print("NO")