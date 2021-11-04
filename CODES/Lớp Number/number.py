
class Number:
    def __init__(self, n1, n2):
        self.number1 = n1
        self.number2 = n2

    def input_info(self):
        mess = f"{self.number1} va {self.number2}"
        print(mess)

    def addition(self):
        res = self.number2 + self.number1
        print(f"Tong: {res}")

    def substract(self):
        res = self.number2 - self.number1
        print(f"Hieu: {res}")

    def multiply(self):
        res = self.number2 * self.number1
        print(f"Tich: {res}")

    def div(self):
        res = self.number2 / self.number1
        print(f"Thuong: {res}")