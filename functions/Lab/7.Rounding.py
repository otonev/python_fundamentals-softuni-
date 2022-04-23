#!/usr/bin/env python

if __name__ == "__main__":
    numbers_list = input().split()
    rounded_list = []
    for number in numbers_list:
        num = round(float(number))
        rounded_list.append(num)
    print(rounded_list)
