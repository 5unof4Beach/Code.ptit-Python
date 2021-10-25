import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, p2):
        width = abs(self.x - p2.x)
        height = abs(self.y - p2.y)
        res = math.sqrt(width**2 + height**2)
        return "{:.4f}".format(res)

    # def Point(self, x, y):
    #     self.x = x
    #     self.y = y


