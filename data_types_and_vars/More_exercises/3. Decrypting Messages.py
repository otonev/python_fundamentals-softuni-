#!/usr/bin/env python

if __name__ == "__main__":
    key = int(input())
    n = int(input())
    string = ''

    for letter in range(n):
        current_letter = input()
        current_letter_enc = ord(current_letter)
        current_letter_dec = current_letter_enc + key
        char = chr(current_letter_dec)
        string += char

    print(string)