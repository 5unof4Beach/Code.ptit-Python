# #Bai 1
# print(5+3,9-1,4*2,24/3)
#
# #Bai 2
# n = 420
# messg = 'so yeu thich cua minh la:'
# print(messg,n)
#
# #Bai 3
# num1 = 6 + 1.2j
# num2 = 9 + 0.6j
#
# print(num1 + num2)
# print(num1 - num2)

# #Bai 4
# s =  """s la mot chuoi gom
# nhieu dong
# viet chuong trinh"""
#
# s = max(s.split('\n'),key=len)
#
# print(s)
#
# bai 5
# a = 'abcd'
# b = '12345'
# print(a[:int(len(a)/2)], b , a[int(len(a)/2):len(a)],sep='')

#bai 6
# s = "Bbc3rt6&7%"
# alpha_up,alpha_low , num , char = 0,0,0,0
#
# for i in s:
#
#     if i.isupper(): alpha_up += 1
#     elif i.islower(): alpha_low += 1
#     elif i.isnumeric(): num += 1
#     else: char += 1
#
# print("So chu hoa:",alpha_up)
# print("So chu thuong:",alpha_low)
# print("So chu so:",num)
# print("So ky tu:",char)
#
# # bai 7
# print("Bai 7")
# n = int(input())
# if(n % 2 == 0):
#     print("Chan")
# else:
#     print("le")

#Bai 1
# print("Bai 1")
# line =['cho','meo','ga','vit']
# del line[-1]
# print(line)
# line.insert(4,'trau')
# print(line)
# line[0] = 'python'
# print(line)
#
# #Bai 2
# print("Bai 2")
# line =['cho','meo','ga','vit']
# line[0],line[-1] = line[-1],line[0]
# print(line)

# #Bai 3
# print("Bai 3")
# line = [1,13,14,16,18,13,21,4]
# arr = []
# for i in line:
#     if i%2 != 0:
#         arr.append(i)
# print(arr)
#
# #Bai 4
# print("Bai 4")
# line = ["1","a","g","t","7","9"]
# print(line)
# sum = 0
# for i in line:
#     if i.isnumeric():
#         sum += int(i)
# print(sum)

#Bai 5
# print("Bai 5")
# line = [1,5,4,6,7,2,3,8]
# # for i in range(len(line)):
# #     line[i] = line[i]**2
# line = [i**2 for i in line]
# line.sort(reverse=True)
# print(line)

#Bai 6
# print("Bai 6")
# arr = [1,"a",34,"a","b",1,"c"]
# arr=set(arr)
# print(len(arr))

# 06/09/2021

# #Bai 1:
# lst = [1,5,1,8,4,1,4,3,2,8,4,9]
# count = [0] * (max(lst) + 1)
# for i in lst:
#     count[i] += 1
# for i in range(len(count)):
#     if(count[i] >= 3):
#         print(i,"",end="")

#Bai 5:
# import math
#
# print("Bai 5 :")
# dat = ("www.z.com","www.fb.org","www.sap.net","www.yt.in")
# res = []
# for i in dat:
#     lst = i.split(".")
#     res.append(lst[-1])
# print(res)
#
# #Bai 6:
# print("Bai 6 :")
# lst = [('a',23),('b',37),('c',11),('d',29)]
# lst_sorted = sorted(lst,key = lambda x:x[1])
# print(lst_sorted)

#Bai 3:
import math

def isPrime(n):
    if  n < 2: return 0
    for i in range(2,int(math.sqrt(n)+1)):
        if n % i == 0: return 0
    return 1

lst = (1,2,3,4,5,6,7,8,9,10)
c = 0
for i in lst:
    if isPrime(i):
        print(i,"",end="")
        c += 1
print("")
print(c)

#bai 4:
arr = [1,2,3]
sum = 0
res = []
for i in arr:
    sum += i
    res.append(sum)
print(res)

