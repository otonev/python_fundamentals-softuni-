#!/usr/bin/env python

if __name__ == "__main__":
    word = input()
    occurrences = {}
    for char in word:
        if char == " ":
            continue
        elif char not in occurrences:
            occurrences[char] = 1
        else:
            occurrences[char] += 1
    for k, v in occurrences.items():
        print(f"{k} -> {v}")
        