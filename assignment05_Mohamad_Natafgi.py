class Course:
    def __init__(self, code, name, credit_num, course_type):
        self.code = code
        self.name = name
        self.credit_num = credit_num
        self.course_type = course_type

    def __str__(self):
        return f"{self.code} - {self.name} ({self.credit_num} credits, {self.course_type})"


class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.enrolled_courses = {}

    def enroll(self, course):
        if course.code in self.enrolled_courses:
            raise ValueError(f"Already enrolled in course {course.code}.")
        self.enrolled_courses[course.code] = course
        print(f"Enrolled in course {course.code} - {course.name}")

    def drop(self, course_code):
        if course_code not in self.enrolled_courses:
            raise ValueError(f"Course {course_code} not found in enrolled courses.")
        del self.enrolled_courses[course_code]
        print(f"Dropped course {course_code}")

    def list_courses(self):
        if not self.enrolled_courses:
            print("No courses enrolled.")
        else:
            for course in self.enrolled_courses.values():
                print(course)


class UniversitySystem:
    def __init__(self):
        self.catalog = {}
        self.students = {}

    def add_course(self):
        code = input("Enter course code: ")
        name = input("Enter course name: ")
        credit_num = int(input("Enter credit hours: "))
        course_type = input("Enter course type (core/elective): ")
        new_course = Course(code, name, credit_num, course_type)
        self.catalog[code] = new_course
        print(f"Course {code} - {name} added to the catalog.")

    def enroll_student(self):
        student_id = input("Enter student ID: ")
        if student_id not in self.students:
            name = input("Enter student name: ")
            self.students[student_id] = Student(student_id, name)
            print(f"Student {name} with ID {student_id} added.")

        course_code = input("Enter course code to enroll in: ")
        if course_code not in self.catalog:
            print("Course not found in catalog.")
            return
        try:
            self.students[student_id].enroll(self.catalog[course_code])
        except ValueError as e:
            print(e)

    def drop_course(self):
        student_id = input("Enter student ID: ")
        if student_id not in self.students:
            print("Student not found.")
            return

        course_code = input("Enter course code to drop: ")
        try:
            self.students[student_id].drop(course_code)
        except ValueError as e:
            print(e)

    def list_student_courses(self):
        student_id = input("Enter student ID: ")
        if student_id not in self.students:
            print("Student not found.")
            return

        print(f"Courses for {self.students[student_id].name}:")
        self.students[student_id].list_courses()

    def save_catalog(self):
        filename = input("Enter filename to save catalog: ")
        with open(filename, "w") as file:
            for course in self.catalog.values():
                file.write(f"{course.code},{course.name},{course.credit_num},{course.course_type}\n")
        print("Course catalog saved.")

    def load_catalog(self):
        filename = input("Enter filename to load catalog: ")
        try:
            with open(filename, "r") as file:
                for line in file:
                    code, name, credit_num, course_type = line.strip().split(",")
                    self.catalog[code] = Course(code, name, int(credit_num), course_type)
            print("Course catalog loaded.")
        except FileNotFoundError:
            print("File not found.")


def main():
    system = UniversitySystem()
    while True:
        print("\nMenu:")
        print("1. Add Course")
        print("2. Enroll Student in Course")
        print("3. Drop Course for Student")
        print("4. List Student Courses")
        print("5. Save Course Catalog")
        print("6. Load Course Catalog")
        print("7. Exit")

        choice = input("Enter choice: ")
        if choice == "1":
            system.add_course()
        elif choice == "2":
            system.enroll_student()
        elif choice == "3":
            system.drop_course()
        elif choice == "4":
            system.list_student_courses()
        elif choice == "5":
            system.save_catalog()
        elif choice == "6":
            system.load_catalog()
        elif choice == "7":
            print("Exiting program.")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
