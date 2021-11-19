from builtins import input

# with open("pi_digits.txt") as input:
#     lines = input.readlines()
# pi = ""
# for line in lines:
#     pi += line.strip()
#
# print(pi)
#
# with open("guest.txt", 'a') as output:
#     output.write("Hello File")

# name = ""
# with open("guest.txt", 'a') as output:
#     while( name != 'quit'):
#         output.write(f"Hello {name}\n")
#         name = input()
#
# ans = "not empty"
# with open("response.txt", 'a') as output:
#     while( ans != ''):
#         output.write(f"answer: {ans}\n")
#         ans = input()

# while True:
#     try:
#         n = int(input())
#     except ValueError:
#         print("thats not a number")
#     else:
#         if n == 0:
#             break
#         print(n)

# while True:
#     file = input() + '.txt'
#     # print(file)
#     str = ""
#     try:
#         with open(file) as fInput:
#             lines = fInput.readlines()
#     except FileNotFoundError:
#         print("there's no such file")
#     else:
#         count = 0
#         for i in lines:
#             count += i.count(" ") + 1
#         print(count)

print("Bai 5")
import json
filename = 'data.json';

dat = {'c':1, 'b':12, 'a':13}
sortedDat = sorted(dat.items())

with open(filename, mode='w') as f:
    json.dump(dat, f, indent=2, sort_keys=True)

print("Bai 6")
filename = 'username.json'
name = ''
with open(filename, mode='r') as f1:
    name = json.load(f1)

print(name)
