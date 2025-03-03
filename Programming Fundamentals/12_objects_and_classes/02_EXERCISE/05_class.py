from numpy.ma.extras import average


class Class:
    __students_counter = 22

    def __init__(self, name):

        self.name = name
        self.students = []
        self.grades = []


    def add_student(self, name: str, grade: float):

        self.students.append(name)
        self.grades.append(grade)
        Class.__students_counter -= 1

    def get_average_grade(self):
        average_grade = sum(self.grades) / len(self.grades)

    def __repr__(self):

        return f"The students in {self.name}: {", ".join(self.students)}.\n"


a_class = Class("11B")
a_class.add_student("Peter", 4.80)
a_class.add_student("George", 6.00)
a_class.add_student("Amy", 3.50)
print(a_class)
