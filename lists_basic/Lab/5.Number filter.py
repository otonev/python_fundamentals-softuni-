#!/usr/bin/env python

if __name__ == "__main__":
    n = int(input())
    numbers = []
    filtered_numbers = []
    for _ in range(n):
        current_num = int(input())
        numbers.append(current_num)
    command = input()
    if command == "even":
        for num in numbers:
            if num % 2 == 0:
                filtered_numbers.append(num)
    elif command == "odd":
        for num in numbers:
            if num % 2 != 1:
                filtered_numbers.append(num)
    elif command == "negative":
        for num in numbers:
            if num < 0:
                filtered_numbers.append(num)
    elif command == "positive":
        for num in numbers:
            if num >= 0:
                filtered_numbers.append(num)
    print(filtered_numbers)