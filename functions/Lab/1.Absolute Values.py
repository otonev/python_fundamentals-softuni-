#!/usr/bin/env python

if __name__ == "__main__":
    def get_absolute(num):
        num = float(num)
        num = abs(num)
        return num


    numbers_list = input().split()
    absolutes = []
    for number in numbers_list:
        absolute_value = get_absolute(number)
        absolutes.append(absolute_value)
    print(absolutes)
