#!/usr/bin/env python

if __name__ == "__main__":
    year=input()
    while len(set(year)) != len(year):
        year = int(year)
        year += 1
        year = str(year)
    print(year)