import math


class Prime:
    def __init__(self, x):
        self.x = x

    def isPrime(self, x):
        if x == 2:
            return False
        for i in range(2, int(math.sqrt(x) + 1)):
            if x % i == 0:
                return False
        return True

    def checkPrime(self):
        if self.isPrime(self.x):
            print("x la so nguyen to")
        else:
            print("x khong la so nguyen to")

    def next_prime(self):
        temp = self.x + 1
        while not self.isPrime(temp):
            temp += 1
        print(temp)

