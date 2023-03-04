class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.rates = {}

    def __str__(self):
        return f"Имя: {self.name}\n" \
               f"Фамилия: {self.surname}\n" \
               f"Средняя оценка за лекции: {round(self.get_avr(), 1)}"

    def __lt__(self, lecturer):
        if isinstance(lecturer, Lecturer):
            return self.get_avr() < lecturer.get_avr()
        else:
            return 'Ошибка сравнения'

    def __le__(self, lecturer):
        if isinstance(lecturer, Lecturer):
            return self.get_avr() <= lecturer.get_avr()
        else:
            return 'Ошибка сравнения'

    def __eq__(self, lecturer):
        if isinstance(lecturer, Lecturer):
            return self.get_avr() == lecturer.get_avr()
        else:
            return 'Ошибка сравнения'

    def __ne__(self, lecturer):
        if isinstance(lecturer, Lecturer):
            return self.get_avr() != lecturer.get_avr()
        else:
            return 'Ошибка сравнения'

    def __gt__(self, lecturer):
        if isinstance(lecturer, Lecturer):
            return self.get_avr() > lecturer.get_avr()
        else:
            return 'Ошибка сравнения'

    def __ge__(self, lecturer):
        if isinstance(lecturer, Lecturer):
            return self.get_avr() >= lecturer.get_avr()
        else:
            return 'Ошибка сравнения'

    def get_avr(self):
        avr_sum = 0
        avr_count = 0
        for course_rates in self.rates.values():
            avr_sum += sum(course_rates)
            avr_count += len(course_rates)
        return avr_sum / avr_count


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        return f"Имя: {self.name}\n" \
               f"Фамилия: {self.surname}\n"

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        return f"Имя: {self.name}\n" \
               f"Фамилия: {self.surname}\n" \
               f"Средняя оценка за домашние задания: {self.get_avr()}\n" \
               f"Курсы в процессе изучения: {', '.join(self.courses_in_progress) or 'нет'}\n" \
               f"Завершенные курсы: {', '.join(self.finished_courses) or 'нет'}"

    def __lt__(self, student):
        if isinstance(student, Student):
            return self.get_avr() < student.get_avr()
        else:
            return 'Ошибка сравнения'

    def __le__(self, student):
        if isinstance(student, Student):
            return self.get_avr() <= student.get_avr()
        else:
            return 'Ошибка сравнения'

    def __eq__(self, student):
        if isinstance(student, Student):
            return self.get_avr() == student.get_avr()
        else:
            return 'Ошибка сравнения'

    def __ne__(self, student):
        if isinstance(student, Student):
            return self.get_avr() != student.get_avr()
        else:
            return 'Ошибка сравнения'

    def __gt__(self, student):
        if isinstance(student, Student):
            return self.get_avr() > student.get_avr()
        else:
            return 'Ошибка сравнения'

    def __ge__(self, student):
        if isinstance(student, Student):
            return self.get_avr() >= student.get_avr()
        else:
            return 'Ошибка сравнения'

    def rate_l(self, lecturer, grade):
        for course in self.courses_in_progress:
            if course in lecturer.courses_attached:
                if lecturer.rates:
                    lecturer.rates[course] += [grade]
                else:
                    lecturer.rates[course] = [grade]

    def get_avr(self):
        avr_sum = 0
        avr_count = 0
        for course_grades in self.grades.values():
            avr_sum += sum(course_grades)
            avr_count += len(course_grades)
        if avr_count == 0:
            return 0
        return avr_sum / avr_count


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']

cool_student = Student('Ruoy', 'Eman', 'your_gender')
cool_student.courses_in_progress += ['Python']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']
cool_reviewer.courses_attached += ['Git']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Git', 10)

cool_reviewer.rate_hw(cool_student, 'Python', 10)

print(f"Студент: {best_student.name} Грейд: {best_student.grades}")

cool_lecturer = Lecturer("Bob", "Smith")
cool_lecturer.courses_attached += ['Python']

best_student.rate_l(cool_lecturer, 8)
best_student.rate_l(cool_lecturer, 7)
best_student.rate_l(cool_lecturer, 10)


print('best_student < cool_student', best_student < cool_student)


def avr_hw(students, course):
    avr_sum = 0
    avr_count = 0
    for student in students:
        grades = student.grades[course]
        avr_sum += sum(grades)
        avr_count += len(grades)
    if avr_count == 0:
        return 0
    return avr_sum / avr_count


print('avr_hw', avr_hw([best_student, cool_student], 'Python'))


def avr_l(lecturers, course):
    avr_sum = 0
    avr_count = 0
    for lecturer in lecturers:
        rates = lecturer.rates[course]
        avr_sum += sum(rates)
        avr_count += len(rates)
    if avr_count == 0:
        return 0
    return avr_sum / avr_count
  
  
print('avr_l', avr_l([cool_lecturer], 'Python'))
