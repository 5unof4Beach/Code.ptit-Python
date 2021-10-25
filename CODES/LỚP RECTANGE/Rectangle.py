
class Rectangle:
    def __init__(self,width,height,color):
        self.width = width
        self.height = height
        self.co = color

    def perimeter(self):
        return 2 * (self.width + self.height)

    def area(self):
        return self.width * self.height

    def color(self):
        return f"{self.co.lower().capitalize()}"


