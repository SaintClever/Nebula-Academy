class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.courses = []

    def display_info(self):
        print(f"Student ID: {self.student_id}")
        print(f"Name: {self.name}")
        print("Courses Enrolled:")
        for course in self.courses:
            print(f" - {course.course_code}: {course.course_name}")
        print()

    def enroll(self, course):
        if course not in self.courses:
            if len(course.students) < course.max_students:
                self.courses.append(course)
                course.enroll_student(self)
                print(f"Enrolled in course {course.course_code}: {course.course_name}.")
            else:
                print(
                    f"Course {course.course_code}: {course.course_name} is full. Enrollment failed."
                )
        else:
            print(
                f"Already enrolled in course {course.course_code}: {course.course_name}."
            )

    def get_courses(self):
        return self.courses


class Course:
    def __init__(self, course_code, course_name, max_students):
        self.course_code = course_code
        self.course_name = course_name
        self.max_students = max_students
        self.students = []

    def display_info(self):
        print(f"Course Code: {self.course_code}")
        print(f"Course Name: {self.course_name}")
        print(f"Max Students: {self.max_students}")
        print("Students Enrolled:")
        for student in self.students:
            print(f" - {student.student_id}: {student.name}")
        print()

    def enroll_student(self, student):
        self.students.append(student)

    def get_students(self):
        return self.students


# Example Usage
student1 = Student(student_id=101, name="Alice")
student2 = Student(student_id=102, name="Bob")

course1 = Course(
    course_code="CS101", course_name="Introduction to Programming", max_students=3
)
course2 = Course(course_code="MATH201", course_name="Calculus", max_students=2)

student1.enroll(course1)
student1.enroll(course2)
student2.enroll(course1)
print()

student1.display_info()
student2.display_info()
print()

course1.display_info()
course2.display_info()
