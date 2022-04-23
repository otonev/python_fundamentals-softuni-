#!/usr/bin/env python

if __name__ == "__main__":
    def repeat_string(word: str, time_to_rep: int):
        return word*time_to_rep


    string = input()
    n = int(input())
    print(repeat_string(string, n))
    