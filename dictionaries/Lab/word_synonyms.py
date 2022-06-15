#!/usr/bin/env python

if __name__ == "__main__":
    n = int(input())
    synonyms = {}
    for _ in range(n):
        word = input()
        synonym = input()
        if word in synonyms:
            synonyms[word].append(synonym)
        else:
            synonyms[word] = [synonym]
    for k, v in synonyms.items():
        print(f"{k} - {', '.join(v)}")
