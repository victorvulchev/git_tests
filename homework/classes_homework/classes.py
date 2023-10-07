class Student():
    counter = 0
    def __init__(self, name= "", course= None, speciality= "", university= "", email= "", phone= 0):
        self.name = name
        self.course = course
        self.speciality = speciality
        self.university = university
        self.email = email
        self.phone = phone
        Student.counter += 1
    def info(self):
        print("Student Information:")
        print(f"Name: {self.name}")
        print(f"Course: {self.course}")
        print(f"Speciality: {self.speciality}")
        print(f"University: {self.university}")
        print(f"Email: {self.email}")
        print(f"Phone: {self.phone}")

std1 = Student("Pesho", "Python", "Programmer")
std2 = Student()
#print(Student.counter)
std1.info()