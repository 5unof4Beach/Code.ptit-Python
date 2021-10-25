from Person import Person
from Student import Student
from Rectangle import Rectangle

r = Rectangle(10, 2)
r.cal_s()
r.cal_p()

print()

s = Student("Duc Bui", "Nam", "30/02/2001", "B19DCCN186", 3.9, "B19CN186@gmail.com")
s.description_student()
s.check_scholarship()