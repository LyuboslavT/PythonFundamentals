class Class:
    __students_counter = 22

    def __init__(self, name):

        self.name = name
        self.students = []
        self.grades = []


    def add_student(self, name: str, grade: float):

        if Class.__students_counter > 0:
            self.students.append(name)
            self.grades.append(grade)
            Class.__students_counter -= 1

    def get_average_grade(self):

        average_grade = float(sum(self.grades) / len(self.grades))
        return average_grade



    def __repr__(self):
        return f"The students in {self.name}: {', '.join(self.students)}.\n" \
               f"Average Grade: {self.get_average_grade():.2f}"

a_class = Class("11B")
a_class.add_student("Peter", 4.80)
a_class.add_student("George", 6.00)
a_class.add_student("Amy", 3.50)
print(a_class)
