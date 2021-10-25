class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def cal_s(self):
        print(f"HCN co dien tich: {self.height * self.width}")

    def cal_p(self):
        print(f"HCN co chu vi: {2 * (self.height + self.width)}")