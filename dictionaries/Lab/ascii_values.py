#!/usr/bin/env python

if __name__ == "__main__":
    chars = input().split(", ")
    characters = {char: ord(char) for char in chars}
    print(characters)
