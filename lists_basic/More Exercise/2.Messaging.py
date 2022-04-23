#!/usr/bin/env python

if __name__ == "__main__":
    numbers = input().split()
    string = list(input())
    message = ''
    for number in numbers:
        sum_digits = 0
        for digit in number:
            digit = int(digit)
            sum_digits += digit

        if len(string) < sum_digits:
            index = sum_digits - len(string)
        else:
            index = sum_digits

        char = string.pop(index)
        message += char

    print(message)
