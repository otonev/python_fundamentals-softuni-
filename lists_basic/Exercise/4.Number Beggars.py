#!/usr/bin/env python

if __name__ == "__main__":
    nums_string = input().split(", ")
    beggars_count = int(input())

    numbers = []
    beggars = []
    index = 0

    for num_string in nums_string:
        number = int(num_string)
        numbers.append(number)

    for i in range(beggars_count):
        beggars.append(0)

    for number in numbers:
        beggars[index] += number
        index += 1

        if index == beggars_count:
            index = 0

    print(beggars)
