#!/usr/bin/env python

if __name__ == "__main__":
    n = int(input())
    sum = 0

    for character in range(n):
        current_char = input()
        sum += ord(current_char)

    print(f'The sum equals: {sum}')
    