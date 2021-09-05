#https://stackoverflow.com/questions/1059559/split-strings-into-words-with-multiple-word-boundary-delimiters
import re
n = int(input())
sentence = []
while n:
    n-=1
    nhap = input().lower()
    temp = []
    #loai bo cac chu so trong chuoi
    line = ''.join([i for i in nhap if not i.isdigit()])

    #loc tu trong cau
    specialChar = re.compile('\W')

    #laai bo di cac ky yu dac biet va chi de lai dau cach
    temp = re.sub(specialChar,' ',line)

    temp = temp.split()
    # temp = re.findall(r"[\w']+",line)
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