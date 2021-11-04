import math

from prime import Prime


class CheckNumber(Prime):
    def __init__(self, x):
        super().__init__(x)
        self.x = x

    def parity_check(self):
        if self.x % 2 == 0:
            print("So nhap vao la so le")
        else:
            print("So nhap vao la so chan")

    def is_perfect(self):
        sum = 0
        for i in range(2, int(math.sqrt(self.x)+1)):
            if self.x % i == 0:
                sum += i
        if sum == self.x:
            print("So da cho la so hoan hao")
        else:
            print("So da cho khong hoan hao")

    def is_square(self):
        a = math.sqrt(self.x)
        b = int(a)
        if (a - b) == 0:
            print("So da nhap la so chinh phuong")
        else:
            print("So da nhap khong la so chinh phuong")
