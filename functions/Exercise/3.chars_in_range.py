#!/usr/bin/env python

if __name__ == "__main__":
    start_char = input()
    end_char = input()


    def chars_in_range(start, end):
        for char in range(ord(start) + 1, ord(end)):
            print(chr(char), end=' ')


    chars_in_range(start_char, end_char)
    