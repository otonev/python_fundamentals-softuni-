#!/usr/bin/env python

if __name__ == "__main__":
    courses = {}
    tokens = input()
    while True:
        tokens = tokens.split(":")
        if len(tokens) >= 3:
            student_name = tokens[0]
            student_id = tokens[1]
            course = tokens[2]
            if course not in courses:
                courses[course] = {}
            courses[course][student_name] = student_id
            tokens = input()
        else:
            break
    searched_course = tokens[0].split("_")
    for info in courses.items():
        if info[0] == " ".join(searched_course):
            for student_name, student_id in info[1].items():
                print(f"{student_name} - {student_id}")
