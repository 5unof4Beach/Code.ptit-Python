print("Bai 2: ")

def is_pp(n):
    sum = 0
    for i in range(1,(n//2)+1):
        if(n % i == 0):
           sum += i

    if(sum > n):
        return True
    else:
        return False

count = 0
num = 18
while True:
    if is_pp(num):
        count += 1
    if count == 49:
        print(num)
        break
    num += 1

count = 0
for i in range(18,250):
    if is_pp(i):
        count += 1
    if count == 49:
        print(num)
        break


print("Bai 3")

def check(s):
    s1 = s[:len(s)//2]
    s2 = s[len(s)//2 + 1:]
    # print(s1,s2)
    if(s1 == s2[::-1]):
        return True
    return False

# while True:
#     s = input("Nhap chuoi")
#     if check(s):
#         print("YES")
#     else:
#         print("NO")

# import re
# print("Bai 4")
# sample = "The most familiar palindromes in English are character-unit palindromes. The characters read the same backward as forward. Some examples of palindromic words are redivider, deified, civic, radar, level, rotor, kayak, reviver, racecar, madam, and refer "
# specialChar = re.compile('\W')
# temp = ''
# temp = re.sub(specialChar,' ',sample)
# temp = temp.split()
# print(temp)
#
# palindrome = {}
#
# for word in temp:
#     if check(word):
#         palindrome[word] = len(word)
#
# sorted_dict = sorted(palindrome.items(),key=lambda x:x[1],reverse=True)
#
# print(sorted_dict[0])
#
# print("Bai 5")
#
# def sum( *args):
#     sum = 0
#     for i in args:
#         sum += i
#
#     print(sum)
#
# sum(1,2,3,4,5)
# print("Bai 6")
# def word_connect(**kwargs):
#     res = ''
#     for val in kwargs.values():
#         res += val
#         res += ' '
#     print(res)
#
# word_connect(args = 'hello',a2 = 'how', a3 = 'low')
#
# print("Bai 7")
def solve1(a,b):
    if a == 0:
        print("pt vô nghiệm")
    elif a != b:
        print("pt có nghiệm duy nhất:", -b/a)
    elif a==0 and b == 0:
        print("pt có vô số nghiệm")

print("bai 8")
import math
def solve2(a,b,c):
    if a==0:
        solve1(b,c)
    else:
        delta = b**2 - 4*a*c
        if delta > 0 :
            x1 = (float)((-b + math.sqrt(delta)) / (2 * a))
            x2 = (float)((-b - math.sqrt(delta)) / (2 * a))
            print("pt có 2 nghiệm là: x1 = ", x1, " và x2 = ", x2)
        elif delta == 0:
            x1 = (-b / (2 * a));
            print("pt có nghiệm kép: x1 = x2 = ", x1)
        else:
            print("pt vô nghiệm")

solve2(1,2,3)