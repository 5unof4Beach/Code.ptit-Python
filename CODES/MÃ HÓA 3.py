sample = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def divide(str):
    str1 = str[:int(len(str)/2)]
    str2 = str[int((len(str)/2)):]
    return str1,str2

def rotate(str):
    k = 0
    res = ''
    for i in str:
        k += sample.find(i)
    for i in str:
        res += sample[(sample.find(i) + k)%26]
    return res


def DRM(str):
    str1,str2 = divide(str)
    str1 = rotate(str1)
    str2 = rotate(str2)
    res = ''
    for i in range(len(str1)):
        res += sample[(sample.find(str1[i]) + sample.find(str2[i])) % 26]
    print(res)
    
n = int(input())
while n:
    n-=1
    line = input()
    DRM(line)


