#!/usr/bin/env python

if __name__ == "__main__":
    numbers = input().split(", ")
    for i in range(len(numbers) - 1, -1, -1):
        current_num = int(numbers.pop(i))
        if current_num == 0:
            numbers.append(current_num)
        else:
            numbers.insert(i, current_num)

    print(numbers)
