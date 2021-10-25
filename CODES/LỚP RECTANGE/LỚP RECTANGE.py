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


arr = input().split()
if int(arr[0]) <= 0 or int(arr[1]) <= 0:
    print("INVALID")
else:
    r = Rectangle(int(arr[0]), int(arr[1]), arr[2])
    print('{} {} {}'.format(r.perimeter(), r.area(), r.color()))
