#!/usr/bin/env python

if __name__ == "__main__":
    n = int(input())
    is_open = False
    is_closed = True
    is_balanced = True
    for char in range(n):
        current_char = input()
        if current_char == "(":
            if is_open:
                is_balanced = False
                break
            is_open = True
            is_closed = False
        elif current_char == ")":
            if is_closed:
                is_balanced = False
                break
            is_open = False
            is_closed = True

    if is_balanced:
        print("BALANCED")
    else:
        print("UNBALANCED")