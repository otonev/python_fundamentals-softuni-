#!/usr/bin/env python

if __name__ == "__main__":
    string = input()

    for letter in string:
        print(f"{letter}{letter}", end="")
