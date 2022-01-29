#!/usr/bin/env python

if __name__ == "__main__":
    string = input()
    string = string.split()
    nums = []
    for num in string:
        nums.append(-int(num))
    print(nums)
