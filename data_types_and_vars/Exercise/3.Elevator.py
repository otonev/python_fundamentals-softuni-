#!/usr/bin/env python

if __name__ == "__main__":
    people = int(input())
    capacity = int(input())
    courses = people // capacity
    if people % capacity != 0:
        courses += 1
    print(courses)