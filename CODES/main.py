print("Bai 11")
line = "he did a a a nothing except camp out where he was told to go and he he father a few children"
word = dict()
line = line.split()
for i in line:
    if i in word:
        word[i] += 1
    else:
        word[i] = 1
res = sorted(word.items(), key = lambda x:x[1],reverse=True)
for i in res:
    if i[1]>3:
        print(i)

print("Bai 12")
# res = sorted(word.values(), key = lambda x:x[1],reverse=True)
print(res[0],res[-1])