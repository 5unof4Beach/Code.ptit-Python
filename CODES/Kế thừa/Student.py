from Person import Person


class Student(Person):
    def __init__(self, name, gender, dob, ID, gpa, email):
        super().__init__(name, gender, dob)
        self.ID = ID
        self.gpa = gpa
        self.email = email

    def description_student(self):
        self.description_person()
        print(f"msv: {self.ID} gpa: {self.gpa} email: {self.email}")

    def check_scholarship(self):
        print("Hoc bong: ",end="")
        if self.gpa > 3.2:
            print("YES")
            return
        print("NO")

