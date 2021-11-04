import math


class Circle:
    def __init__(self, x, y, R):
        self.x = x
        self.y = y
        self.R = R

    def describe(self):
        print(f"Hình tròn tâm O({self.x},{self.y}) ban kinh {self.R}")

    def get_area(self):
        s = math.pi * self.R**2
        print(f"Dien tich hinh tron la: {s}")

    def get_perimeter(self):
        p = 2 * math.pi * self.R
        print(f"Chu vi hinh tron la: {p}")
