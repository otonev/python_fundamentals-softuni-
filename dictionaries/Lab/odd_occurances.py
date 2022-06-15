#!/usr/bin/env python

if __name__ == "__main__":
    words = input().split()
    words_dict = {}
    for word in words:
        word = word.lower()
        if word in words_dict:
            words_dict[word] += 1
        else:
            words_dict[word] = 1
    odd_occurances = [key for key, value in words_dict.items() if words_dict[key] % 2 != 0]
    for word in odd_occurances:
        print(word, end=" ")
