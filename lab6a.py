#!/usr/bin/env python3
# Author ID: k62

class Student:
    def __init__(self, name, number):
        self.name = name
        self.number = str(number)  # Make sure that the student number is always a string
        self.courses = {}

    def displayStudent(self):
        return f'Student Name: {self.name}\nStudent Number: {self.number}'

    def addGrade(self, course, grade):
        self.courses[course] = grade

    def displayGPA(self):
        if not self.courses:
            return f'GPA of student {self.name} is 0.0'
        gpa = sum(self.courses.values()) / len(self.courses)
        return f'GPA of student {self.name} is {gpa:.1f}'

    def displayCourses(self):
        passed_courses = [course for course, grade in self.courses.items() if grade > 0.0]
        return passed_courses

if __name__ == '__main__':
    # Create first student object
    student1 = Student('John', 13454900)
    student1.addGrade('uli101', 1.0)
    student1.addGrade('ops245', 2.0)
    student1.addGrade('ops445', 3.0)

    # Create second student object
    student2 = Student('Jessica', 123456)
    student2.addGrade('ipc144', 4.0)
    student2.addGrade('cpp244', 3.5)
    student2.addGrade('cpp344', 0.0)

    # Display student1 information
    print(student1.displayStudent())
    print(student1.displayGPA())
    print(student1.displayCourses())

    # Display student2 information
    print(student2.displayStudent())
    print(student2.displayGPA())
    print(student2.displayCourses())
