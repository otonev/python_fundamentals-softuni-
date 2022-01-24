#!/usr/bin/env python

if __name__ == "__main__":
    n = int(input())
    courses = []
    for _ in range(0,n):
        current_course = input()
        courses.append(current_course)
    print(courses)