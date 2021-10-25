class Person:
    def __init__(self, name, gender, dob):
        self.name = name
        self.gender = gender
        self.dob = dob

    def description_person(self):
        print(f"{self.name} gioi tinh {self.gender} sinh ngay {self.dob} ")