#!/usr/bin/env/python
if __name__ == "__main__":
    text = input()
    forbidden_chars = ["a", "e", "i", "o", "u"]
    no_vowels = [char for char in text if char not in forbidden_chars]
    print("".join(no_vowels))