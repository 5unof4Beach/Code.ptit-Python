# print("Bai 5")
# n  = int(input())
# sum = 0
# f1 = 0
# f2 = 1
# print(f1,f2,sep = " ",end=" ")
# while sum<=30:
#     print(sum,sep = " ",end=" ")
#     sum = f1 +f2
#     f1,f2 = f2,sum

print("Bai 6")
inp = '0100,0011,1010,1001,1100,1001'
line = []
line = [i for i in inp.split(",")]
for i in line:
    if int(i,2) % 10 == 0:
        print(i)