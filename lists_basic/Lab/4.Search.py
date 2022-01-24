#!/usr/bin/env python

if __name__ == "__main__":
    words = list()
    n = int(input())
    word = input()
    for _ in range(n):
        current_word = input()
        words.append(current_word)
    print(words)
    for i in range(len(words) - 1,-1,-1):
        current_word = words[i]
        if word not in current_word:
            words.remove(current_word)
    print(words)
