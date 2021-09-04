t = int(input())
import math
import itertools
while t:
    t-=1
    def divByThree(n):
        if n%3 ==0:
            return 1
        return 0

    n = input()
    sum = 0
    for i in n:
        sum += int(i)
    if divByThree(sum):
        print("YES")
    else:
        print("NO")