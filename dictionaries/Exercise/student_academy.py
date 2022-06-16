#!/usr/bin/env python

if __name__ == "__main__":
    n = int(input())
    grades = {}

    def add_grade(student, grade_to_add, diary):
        if student not in diary:
            diary[student] = [grade_to_add]
        else:
            diary[student].append(grade_to_add)

    for _ in range(n):
        student_name = input()
        grade = float(input())
        add_grade(student_name, grade, grades)

    to_graduate = {student: sum(grades) / len(grades) for student, grades in grades.items() if sum(grades) / len(grades) >= 4.5}

    for student, average_grade in to_graduate.items():
        print(f"{student} -> {average_grade:.2f}")
