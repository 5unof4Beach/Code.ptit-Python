line = input()
arr = line.split()
q = []
for i in arr:
    if i.isnumeric():
        q.append(int(i))

print(q)