#!/usr/bin/env python

if __name__ == "__main__":
    contests_input = input()
    contests_info = {}

    def read_contest(name, password, dictionary):
        dictionary[name] = password

    def validate_exam_access(exam, passwd, all_exams):
        if exam in all_exams and passwd == all_exams[exam]:
            return True
        return False

    def read_participants(student_name, exam, result, collection):
        if student_name not in collection:
            collection[student_name] = {}
        if exam not in collection[student_name]:
            collection[student_name][exam] = result
        elif exam in collection[student_name]:
            if collection[student_name][exam] < result:
                collection[student_name][exam] = result

    while contests_input != "end of contests":
        tokens = contests_input.split(":")
        contest_name = tokens[0]
        contest_pass = tokens[1]
        read_contest(contest_name, contest_pass, contests_info)
        contests_input = input()

    participant_info = input()
    participants = {}

    while participant_info != "end of submissions":
        tokens = participant_info.split("=>")
        exam_name = tokens[0]
        exam_pass = tokens[1]
        submitter = tokens[2]
        points = int(tokens[3])
        if validate_exam_access(exam_name, exam_pass, contests_info):
            read_participants(submitter, exam_name, points, participants)
        else:
            participant_info = input()
            continue
        participant_info = input()

    best_student = {"name": "", "score": 0}

    for student in participants.keys():
        result = sum(participants[student].values())
        if result > best_student["score"]:
            best_student["name"] = student
            best_student["score"] = result

    print(f"Best candidate is {best_student['name']} with total {best_student['score']} points.")
    print("Ranking:")
    sorted_participants = sorted(participants.keys())
    for participant in sorted_participants:
        print(participant)
        exams_sorted = {k: v for k, v in sorted(participants[participant].items(), key=lambda x: x[1], reverse=True)}
        for k, v in exams_sorted.items():
            print(f"#  {k} -> {v}")
