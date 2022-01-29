#!/usr/bin/env python

if __name__ == "__main__":
    import sys

    nums_string = input().split()
    nums_to_remove = int(input())
    numbers = []
    lowes_num = sys.maxsize

    for num_string in nums_string:
        numbers.append(int(num_string))

    for _ in range(nums_to_remove):
        for number in numbers:
            if number < lowes_num:
                lowes_num = number

        numbers.remove(lowes_num)
        lowes_num = sys.maxsize
    print(", ".join([str(i) for i in numbers]))

