class Student:
    def __init__(self, name, ID, Cl):
        self.name = name
        self.ID = ID
        self.Cl4ss = Cl

    def descripton_student(self):
        print("Name:", self.name)
        print("ID:", self.ID)
        print("Class:", self.Cl4ss)

    def descripton_object(self, monhoc):
        print(monhoc)


s = Student("Bui Minh Duc", "B19DCCN186", "D19CQCN06-B")
s.descripton_student()
s.descripton_object("Python Programming")