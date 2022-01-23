#!/usr/bin/env python

if __name__ == "__main__":
    start_char = int(input())
    end_char = int(input())

    for char in range(start_char, end_char + 1):
        print(chr(char), end=' ')