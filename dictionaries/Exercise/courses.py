#!/usr/bin/env python

if __name__ == "__main__":
    curriculum = {}
    command = input()

    def validate_curriculum(curriculum_dict, course_to_check):
        if course_to_check not in curriculum_dict:
            curriculum_dict[course_to_check] = []

    def register_student(student_names, course_to_register, curriculum_dict):
        curriculum_dict[course_to_register].append(student_names)

    def print_curriculum(curriculum_dict):
        for k,v in curriculum_dict.items():
            print(f"{k}: {len(v)}")
            for student in v:
                print(f"-- {student}")

    while command != "end":
        tokens = command.split(" : ")
        course_name = tokens[0]
        student_name = tokens[1]
        validate_curriculum(curriculum, course_name)
        register_student(student_name, course_name, curriculum)
        command = input()

    print_curriculum(curriculum)
