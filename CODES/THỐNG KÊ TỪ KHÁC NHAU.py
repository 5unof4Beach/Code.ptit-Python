#https://stackoverflow.com/questions/1059559/split-strings-into-words-with-multiple-word-boundary-delimiters
import re
n = int(input())
sentence = []
while n:
    n-=1
    line = input().lower()
    temp = []
    #loc tu trong cau
    temp = re.findall(r"[\w']+",line)
    for i in temp:
        sentence.append(i)

#sap xep theo tu dien
sentence.sort()
hash = dict()

for i in sentence:
    if i in hash:
        hash[i] += 1
    else:
        hash[i] = 1

# sap xep hash theo value
hash_sorted = sorted(hash.items(), key = lambda x:x[1],reverse=True)

for i in hash_sorted:
    print(i[0],i[1])